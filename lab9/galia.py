import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from PIL import ImageOps
from fourier import plot_fourier, find_pattern

# load, invert and to greyscale
galia = np.asarray(ImageOps.invert(Image.open("res/galia.png").convert("L")))
e = np.asarray(ImageOps.invert(Image.open("res/e.png").convert("L")))

plot_fourier(galia)

threshold = 0.9
classification = find_pattern(galia, e, threshold)

# mark found letters
mark_e = np.array(Image.open("res/galia.png").convert("RGB"))
h, w = e.shape
e_count = 0
for i in range(classification.shape[0]):
    for j in range(classification.shape[1]):
        if classification[i, j]:
            e_count += 1
            mark_e[i-h:i, j] = (255, 0, 0)
            mark_e[i-h:i, j-w] = (255, 0, 0)
            mark_e[i, j-w:j] = (255, 0, 0)
            mark_e[i-h, j-w:j] = (255, 0, 0)

plt.imshow(mark_e)
plt.title(f"threshold {threshold}, found {e_count} 'e'")
plt.show()
print(f"found {e_count} 'e'")

# save result
result = Image.fromarray(mark_e)
result.save("out/galia_result.jpg")
