.. _tutorials:

Tutorials
=========

As part of the James Webb Space Telescope’s (JWST) Early Release Programs, we have a goal of demonstrating JWST’s capabilities and swiftly disseminating them to the community.
The following tutorials aim to do that by providing simple walkthroughs of our ability to reveal exoplanets in imaged extrasolar systems with the post-processing algorithm pyKLIP.
Beginners should start with our NIRCAM_F300M_Basic_KLIP_Subtraction, which takes you through the process of modeling and subtracting excess starlight from an image in order to uncover two fake underyling planets. 
To get a quantitative estimate of how well JWST will do imaging exoplanets, take a look at our NIRCAM_F300M_ContrastCurves tutorial, 
which uses pyKLIP's algorithms to inject fake planets into simulated data, and estimate how well we'll be able to recover them at various separations from the host star.
Finally, you can use the NIRCAM_F300M_BKA_Outer_Planet tutorial to see how we'd use our knowledge of a planet's existence in our data to estimate its flux and position relative to the host star. 



.. toctree::
   :maxdepth: 1

   tutorials/NIRCAM_F300M_Basic_KLIP_Subtraction
   tutorials/NIRCAM_F300M_ContrastCurves.ipynb
   tutorials/NIRCAM_F300M_BKA_Outer_Planet
