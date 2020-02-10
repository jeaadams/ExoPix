import os
import astropy.io.fits as fits
import numpy as np
import scipy
import scipy.ndimage as ndi
import matplotlib.pylab as plt
import pandas as pd
import pyklip.klip
import pyklip.instruments.Instrument as Instrument
import pyklip.parallelized as parallelized
import pyklip.rdi as rdi
import pyklip.fakes as fakes
from astropy.nddata.utils import Cutout2D

#Import the dataset to be used
filtername = "f300m"

parent_directory = os.path.dirname(__file__)


# read in roll 1
with fits.open(parent_directory + "/old_simulated_data/NIRCam_target_Roll1_{0}.fits".format(filtername)) as hdulist:
    roll1_cube = hdulist[0].data

# read in roll 2
with fits.open(parent_directory + "/old_simulated_data/NIRCam_target_Roll2_{0}.fits".format(filtername)) as hdulist:
    roll2_cube = hdulist[0].data  

# combine the two rows
full_seq = np.concatenate([roll1_cube, roll2_cube], axis=0)

# two rolls are offset 10 degrees
pas = np.append([0 for _ in range(roll1_cube.shape[0])], [10 for _ in range(roll2_cube.shape[0])])

# for each image, the (x,y) center where the star is is just the center of the image
centers = np.array([np.array(frame.shape)/2. for frame in full_seq])

# give it some names, just in case we want to refer to them
filenames = np.append(["roll1_{0}".format(i) for i in range(roll1_cube.shape[0])],
                      ["roll2_{0}".format(i) for i in range(roll1_cube.shape[0])])

#Define dataset
dataset = Instrument.GenericData(full_seq, centers, IWA=4, parangs=pas, filenames=filenames)
dataset.flipx = False


# read in unocculted PSF
with fits.open(parent_directory + "/old_simulated_data/NIRCam_unocculted_{0}.fits".format(filtername)) as hdulist:
    psf_cube = hdulist[0].data 
    psf_head = hdulist[0].header
    
# collapse reference psf in time
psf_frame = np.nanmean(psf_cube, axis=0)

# find the centroid
bestfit = pyklip.fakes.gaussfit2d(psf_frame, 71, 30, searchrad=3, guessfwhm=2, guesspeak=1, refinefit=True)

psf_xcen, psf_ycen = bestfit[2:4]

# recenter PSF to that location
x, y = np.meshgrid(np.arange(-20,20.1,1), np.arange(-20,20.1,1))
x += psf_xcen
y += psf_ycen

psf_stamp = scipy.ndimage.map_coordinates(psf_frame, [y,x])


#Let's choose our contrasts so that the planets get fainter as we go further from the star
psf_stamp_input = np.array([psf_stamp for j in range(12)])
input_contrasts = [1e-3, 7e-4, 3e-4]
planet_seps = [15, 25, 47]
pas = [0, 90, 180, 270]

#Now injecting the fake planets in a spiral:
for input_contrast, planet_sep in zip(input_contrasts, planet_seps):
    planet_fluxes = psf_stamp_input*input_contrast
    
    for pa in pas:
        pyklip.fakes.inject_planet(frames = dataset.input, 
                            centers=dataset.centers, 
                            inputflux=planet_fluxes, 
                            astr_hdrs=dataset.wcs, 
                            radius=planet_sep,
                            pa = pa)

plt.imshow(dataset.input[0], interpolation="nearest", cmap="inferno")

 #Set output directory
outputdir = parent_directory + '/contrastcurves'
fileprefix = 'FAKE_KLIP_ADI_A9K5S1M1'
numbasis = [1,5,10,20,50]


#Run KLIP on dataset with injected fakes
parallelized.klip_dataset(dataset, 
                          outputdir=outputdir, 
                          fileprefix=fileprefix, 
                          algo = 'klip', 
                          annuli=1, 
                          subsections=1, 
                          movement=1, 
                          numbasis=numbasis, 
                          mode="ADI")

#Obtain the centers of the output KLIP fits file
with fits.open(parent_directory + "/contrastcurves/FAKE_KLIP_ADI_A9K5S1M1-KLmodes-all.fits") as hdulist:
    cube = hdulist[0].data
    cube_centers = [hdulist[0].header['PSFCENTX'], hdulist[0].header['PSFCENTY']]

#Create and empty list to store retrieved flux values
retrieved_fluxes = []

#Retrieve planet fluxes
for input_contrast, planet_sep in zip(input_contrasts, planet_seps):
    
    fake_planet_fluxes = []
                                      
    for pa in pas:
        fake_flux = fakes.retrieve_planet_flux(frames = cube[2], 
                                            centers = cube_centers,
                                            astr_hdrs = dataset.wcs[0], 
                                            sep = planet_sep,
                                            pa = pa)
        fake_planet_fluxes.append(fake_flux)

    retrieved_fluxes.append(fake_flux)
    
