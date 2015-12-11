# Teaching Notebooks

I am relatively new to Jupyter notebooks, but I have found them to be an absolutely incredible tool to lower barriers to entry in the quantitative modeling of earth systems. That is because they enable such a seamless integration of text, code and figures, and allow users to tinker with the code without having to know how to write it from scratch.

This repository is work in progress, documenting my own journey in Python and Jupyter.

In this initial version, you will find 3 labs:

1. [ZeroD.ipynb](ZeroD.ipynb) implements a zero-dimensional model of Earth's climate, closely following [Pierrehumbert et al, 2011](http://www.annualreviews.org/doi/abs/10.1146/annurev-earth-040809-152447)

2. [lorenz_climatechange.ipynb](teaching_notebooks/lorenz_climatechange.ipynb) provides a nonlinear dynamical perspective on climate change, emulating much of the analysis of [Palmer (1999}](https://www.researchgate.net/publication/235703704_A_Nonlinear_Dynamical_Perspective_on_Climate_Prediction).  The ODE solver for the Lorenz system was gratefully borrowed from the amazing [jakevdp](https://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/).

3. **ENSO_recharge.ipynb** implements [Jin (1997)](http://yly-mac.gps.caltech.edu/AGU/AGU_2008/Zz_Others/Li_agu08/Jin1997a.pdf)'s "recharge oscillator" model for El Niño-Southern Oscillation.

All labs were geared for Earth Science undergraduates with little to no mathematical background, so they skirt around the analysis and go straight to the "tinkering" part. I will not advocate it as a desirable way to teach Earth Science as a whole, but I have found it useful in generating student interest towards more math-heavy classes so they can understand these concepts at a deeper level. Give it a spin and see if you like it.
