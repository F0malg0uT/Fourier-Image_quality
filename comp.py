import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# Uploading an image (instead of car.jpg, enter the image you need)
img = np.array(Image.open('car.jpg').convert('L')).astype(float)

# Fourier transform 
fft = np.fft.fft2(img)
magnitudes = np.abs(fft)

a = float(input('enter the lower limit of the saved coefficients (%):'))
# Fraction of the saved coefficients
fractions = np.linspace(a*0.01, 1.0, 20)
measure = [] 

for frac in fractions:
    # Here we find the threshold value of the amplitude to preserve the top frac coefficients
    threshold = np.sort(magnitudes.flatten())[int((1 - frac) * magnitudes.size)] #flatten transforms a 2D array into a one-dimensional vector
    # Creating a mask: 1 for coefficients above the threshold, 0 for the rest
    mask = magnitudes > threshold

    # Restoring the image
    reconstructed = np.fft.ifft2(fft * mask).real

    # Creating an image for comparison
    if frac == fractions[0]:
        recon = reconstructed

    # Calculating the MSE (some image quality score)
    measure.append(np.mean(((img - reconstructed)**2) / img))



# Graph

# plt.plot(fractions, measure, 'b-o')
# plt.xlabel('Fraction of the save coefficients')
# plt.ylabel('MSE (ошибка)')
# plt.title('recovery quality')
# plt.grid(True)
# plt.show()

# Рисуем изображения для сравнения
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# There are Settings for changing images 
im0 = axes[0].imshow(img, cmap='gray', vmin=min(img.min(), recon.min()), vmax=max(img.max(), recon.max()))
axes[0].set_title('Original image')
axes[0].axis('off')  # Here we hide axis

im1 = axes[1].imshow(recon, cmap='gray', vmin=min(img.min(), recon.min()), vmax=max(img.max(), recon.max()))
axes[1].set_title('Reconstructed image')
axes[1].axis('off')


# fig.colorbar(im1, ax=axes.ravel().tolist(), shrink=0.5)

plt.show()