.. JWST ERS Pipeline documentation master file, created by
   sphinx-quickstart on Mon Aug  3 01:13:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ExoPlans
=========

ImageWebb is a collection of tutorials aimed at demonstrating the application of the PSF-subtraction algorithm pyKLIP to data collected with the James Webb Space Telescope.
These tutorials provide simple walkthroughs of pyKLIP's ability to reveal exoplanets and measure their properties in simulated JWST data of imaged extrasolar systems.
We recommend starting with our NIRCAM_F300M_Basic_KLIP_Subtraction, which takes you through the process of modeling and subtracting excess starlight from an image in order to
uncover two fake underyling planets. 
To get a quantitative estimate of how well JWST will do imaging exoplanets, take a look at our NIRCAM_F300M_ContrastCurves tutorial, 
which uses pyKLIP's algorithms to inject fake planets into simulated data, and estimate how well we'll be able to recover them at various separations from the host star.
Finally, you can use the NIRCAM_F300M_BKA_Outer_Planet tutorial to see how we'd use our knowledge of a planet's existence in our data to estimate its flux and position relative to the host star. 

Tutorials
---------

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   installation
   tutorials/NIRCAM_F300M_Basic_KLIP_Subtraction
   tutorials/NIRCAM_F300M_ContrastCurves.ipynb
   tutorials/NIRCAM_F300M_BKA_Outer_Planet



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
