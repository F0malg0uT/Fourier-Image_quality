# Fourier-Image_quality
This program tests how much the image quality degrades if we cut off the smallest terms in the Fourier spectrum of the image.

The Fourier spectrum of an image is a representation of an image in the frequency domain that shows
what frequencies of sinusoidal oscillations (or spatial frequencies) are present in the image and with 
what amplitude. The Fourier transform allows a complex image to be decomposed into simpler components - 
sinusoids of different frequencies, which gives a spectrum where each point corresponds to a certain 
spatial frequency and its "strength".

The inverse Fourier transform completely restores the original image. If only some fraction of the
coefficients are left in the Fourier image, the image will be restored with a loss of quality, and the
difference will be greater the fewer coefficients are saved.It is important to note that the larger the
Fourier coefficients in modulus, the greater their contribution to the image quality. This program solves
the problem of finding the optimal number of retained coefficients. The relative difference is taken as a
measure of the restoration quality:

(original - reconstructed)^2 / original

To obtain the image quality level that satisfies the user, choose the initial parameter (lower limit 
of the proportion of coefficients left).

To plot the image restoration quality as a function of the fraction of Fourier coefficients retained you 
need to uncomment lines 39–44.

