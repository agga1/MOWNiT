import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from zad1.Sets import find_disjoint
from zad1.fourier import find_pattern, plot_fourier

image_name = "../res/school.jpg"
pattern_name = "../res/fish1.png"
result_name = "../out/fish_result.jpg"

school = np.asarray(Image.open(image_name).convert("RGB"))
school_red = school[:, :, 0]  # extracting only red channel (most significant)

fish = np.asarray(Image.open(pattern_name).convert("RGB"))
fish_red = fish[:, :, 0]

plot_fourier(school_red)
# find correlation between fish and school (in freq dim)
threshold = 0.2
classification = find_pattern(school_red, fish_red, threshold)

# mark found fish
mark_classified = np.array(Image.open(image_name).convert("RGB"))
h, w = fish_red.shape
for i in range(classification.shape[0]):
    for j in range(classification.shape[1]):
        if classification[i, j]:
            # we want "center" of correlation, not lower right corner
            x = max(i-h//2, 0)
            y = max(j-w//2, 0)
            mark_classified[x, y][0] = 255
            mark_classified[x, y][2] /= 3  # better visibility

plt.imshow(mark_classified)
plt.title(f"{threshold}")
plt.show()

# count fish using disjoint set union
leaders = find_disjoint(classification)

# mark leaders on image
mark_leaders = np.array(Image.open(image_name).convert("RGB"))
for i, j in leaders:
    mark_leaders[i - 3:i + 3, j - 3:j + 3] = [255, 0, 0]

print(f"found {len(leaders)} fish")
plt.imshow(mark_leaders)
plt.title(f"found {len(leaders)} fish")
plt.show()

# save result
result = Image.fromarray(mark_classified)
result.save(result_name)