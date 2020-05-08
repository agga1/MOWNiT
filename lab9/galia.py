import matplotlib.pyplot as plt
import numpy as np
from numpy import fft, rot90, multiply
from PIL import Image
from PIL import ImageOps

# load, invert and to greyscale
galia_img = ImageOps.invert(Image.open("galia.png").convert("L"))
# 2-dim fourier transform
galia = fft.fft2(np.asarray(galia_img))

# plot absolutes
absolute_matrix = np.log10(np.abs(galia))  # log scale, since without it the image will be entirely black
plt.imshow(absolute_matrix, cmap="gray")
plt.show()

# plot phases
phase_matrix = np.angle(galia)
plt.imshow(phase_matrix, cmap="gray")
plt.show()


letter = np.asarray(ImageOps.invert(Image.open("e.png").convert("L")))
letter_x = letter.shape[0]
letter_y = letter.shape[1]
w, h = galia.shape
letter = fft.fft2(rot90(letter, 2), s=(w, h))

#---
mx = np.angle(letter)
plt.imshow(mx, cmap="gray")
plt.show()
# ----
absolute_correlations = abs(fft.ifft2(multiply(galia, letter)))
# ---
mx = absolute_correlations
plt.imshow(mx, cmap="gray")
plt.show()
# ----
max_correlation = np.amax(absolute_correlations)
new_img = np.array(Image.open("galia.png").convert("RGB"))

e_count = 0
for i in range(absolute_correlations.shape[0]):
    for j in range(absolute_correlations.shape[1]):
        if absolute_correlations[i, j] >= 0.9 * max_correlation:
            e_count += 1
            for k in range(letter_x):
                new_img[i-k, j] = (255, 0, 0)
                new_img[i-k, j-letter_y] = (255, 0, 0)
            for l in range(letter_y):
                new_img[i, j-l] = (255, 0, 0)
                new_img[i-letter_x, j-l] = (255, 0, 0)

result = Image.fromarray(new_img)
result.save("new_galia.jpg")
print(e_count)