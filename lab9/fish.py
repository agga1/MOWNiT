import matplotlib.pyplot as plt
import numpy as np
from numpy import fft, rot90, multiply
from PIL import Image
from skimage.morphology import skeletonize

img = np.asarray(Image.open("res/school.jpg").convert("RGB"))
# img = np.asarray(Image.open("res/school.jpg").convert("L"))

school_of_fish = img[:, :, 0]  # only red channel
# school_of_fish = img

print(school_of_fish.shape)
# plt.imshow(school_of_fish)
# plt.show()
school_of_fish = fft.fft2(school_of_fish)

# plot absolutes
# absolute_matrix = np.log10(np.abs(school_of_fish)).astype(np.float64)
# plt.imshow(absolute_matrix, cmap="gray")
# plt.show()

# plot phases
# phase_matrix = np.angle(school_of_fish)
# plt.imshow(phase_matrix, cmap="gray")
# plt.show()


fish = np.asarray(Image.open("res/fish1.png").convert("RGB"))[:, :, 0]
fish_shape = fish.shape
# fish = np.asarray(Image.open("res/fish1.png").convert("L"))

w, h = school_of_fish.shape
fish = fft.fft2(rot90(fish, 2), s=(w, h))

corr = abs(fft.ifft2(multiply(school_of_fish, fish)))
max_correlation = np.amax(corr)
plt.imshow(corr, cmap="gray")
plt.show()
ratio = 0.18

new_img = np.array(Image.open("res/school.jpg").convert("RGB"))
for i in range(corr.shape[0]):
    for j in range(corr.shape[1]):
        if corr[i, j] >= ratio * max_correlation:
            # we want "center" of correlation, not lower right corner
            x = max(i-fish_shape[0]//2, 0)
            y = max(j-fish_shape[1]//2, 0)
            new_img[x, y][0] = 255
            new_img[x, y][2] /= 3

plt.imshow(new_img)
plt.title(f"{ratio}")
plt.show()
# result = Image.fromarray(new_img)
# result.save("new_school_of_fish.jpg")
# count fish
corr_bin = (corr >= ratio * max_correlation) * 1  # binary array

class DisjointUnionSets:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [0] * n
        self.n = n
        for i in range(self.n):
            self.parent[i] = i

    def find(self, x):
        if self.parent[x] != x:
            parent = self.find(self.parent[x])
            self.parent[x] = parent
            return parent
        return x

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot

        elif self.rank[yRoot] < self.rank[xRoot]:
            self.parent[yRoot] = xRoot

        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] = self.rank[xRoot] + 1


sets = DisjointUnionSets(corr_bin.shape[0]*corr_bin.shape[1])
xs, ys = corr_bin.shape
for i in range(xs):
    for j in range(ys):
        if corr_bin[i, j] == 0:
            continue
        for currx in range(max(0, i-1), min(xs, i + 2)):
            for curry in range(max(0, j - 1), min(ys, j + 2)):
                if currx == i and curry == j:
                    continue
                if corr_bin[currx, curry] == 1:
                    sets.union(i * ys + j, currx * ys + curry)
count =0
new_img = np.array(Image.open("res/school.jpg").convert("RGB"))

for i in range(xs):
    for j in range(ys):
        if corr_bin[i,j]==1 and sets.parent[i*ys+j] == i*ys+j:
            count+=1
            new_img[i-2:i+2, j-2:j+2] = [255, 0, 0]

print(count)
plt.imshow(new_img)
plt.show()