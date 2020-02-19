import os
import astropy.io.fits as fits
import numpy as np
import scipy
import scipy.ndimage as ndi
import matplotlib.pylab as plt
import pyklip.klip
import pyklip.instruments.Instrument as Instrument
import pyklip.parallelized as parallelized
import pyklip.rdi as rdi
import pyklip.fakes as fakes
import glob
from astropy.table import Table
from astropy.table import join
from astropy.table import vstack
import pandas as pd
import pdb

parent_directory = os.path.dirname(__file__)
filtername = "f300m"
# read in unocculted PSF
with fits.open(parent_directory + "/old_simulated_data/NIRCam_unocculted_{0}.fits".format(filtername)) as hdulist:
    psf_cube = hdulist[0].data 
    psf_head = hdulist[0].header
    
# collapse reference psf in time
psf_frame = np.nanmean(psf_cube, axis=0)

# find the centroid
bestfit = fakes.gaussfit2d(psf_frame, 71, 30, searchrad=3, guessfwhm=2, guesspeak=1, refinefit=True)

psf_xcen, psf_ycen = bestfit[2:4]

# recenter PSF to that location
x, y = np.meshgrid(np.arange(-20,20.1,1), np.arange(-20,20.1,1))
x += psf_xcen
y += psf_ycen

psf_stamp = scipy.ndimage.map_coordinates(psf_frame, [y,x])

#Import the dataset to be used

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
centers = np.array([np.array(frame.shape)//2. for frame in full_seq])

# give it some names, just in case we want to refer to them
filenames = np.append(["roll1_{0}".format(i) for i in range(roll1_cube.shape[0])],
                      ["roll2_{0}".format(i) for i in range(roll1_cube.shape[0])])

#Define dataset
dataset = Instrument.GenericData(full_seq, centers, IWA=4, parangs=pas, filenames=filenames)
dataset.flipx = False
mask210 = pd.read_csv(parent_directory + '/MASK210R.csv')
def transmission_corrected(input_stamp, input_dx, input_dy):
    distance_from_center = np.sqrt((input_dx)**2+(input_dy)**2)
    trans_at_dist = np.interp(distance_from_center, np.array(mask210["rad_dist"]),
                                     np.array(mask210["trans"]))
    transmission_stamp = trans_at_dist.reshape(input_stamp.shape)
    output_stamp = transmission_stamp*input_stamp
    return output_stamp

#Let's choose our contrasts so that the planets get fainter as we go further from the star
psf_stamp_input = np.array([psf_stamp for j in range(12)])
input_contrasts = [1e-3, 7e-4, 3e-4]
#Remember to only inject 30 or below so it doens't break. 
planet_seps = [35, 35, 35]
pas = [0, 90, 180, 270]

#Now injecting the fake planets in a spiral:
for input_contrast, planet_sep in zip(input_contrasts, planet_seps):
    print(input_contrast)
    planet_fluxes = psf_stamp_input*input_contrast
    
    for pa in pas:
        fakes.inject_planet(frames = dataset.input, 
                            centers=dataset.centers, 
                            inputflux=planet_fluxes, 
                            astr_hdrs=dataset.wcs, 
                            radius=planet_sep,
                            pa = pa,
                            field_dependent_correction = transmission_corrected)

plt.imshow(dataset.input[0], interpolation="nearest", cmap="inferno")
