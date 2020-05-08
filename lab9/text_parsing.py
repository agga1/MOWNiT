import matplotlib.pyplot as plt
import numpy as np
from numpy import fft, rot90, multiply
from PIL import Image
from PIL import ImageOps
from math import trunc
text_name = "cn150.png"
alphabet_name = "cn_sep_b.png"
alphabet = np.asarray(ImageOps.invert(Image.open(alphabet_name).convert("L")))
alphabet = alphabet[:-1, 3:-2]
# alphabet = alphabet[:, 2:-2]
print(alphabet.shape)
lwidth_true = alphabet.shape[1] / (35+34)  # true letter length
lwidth = trunc(lwidth_true)  # unified int letter length
lheight = alphabet.shape[0]
print(lwidth, lheight)
letters = []
for i in range(0, 35+34, 2):
    fr = trunc(lwidth_true * i)
    to = trunc(lwidth_true * (i + 1))
    a = alphabet[:, fr:to]
    if a.shape[1] > lwidth:
        a = a[:, 1:]
    letters.append(a)
    # plt.imshow(a, cmap="gray")
    # plt.show()


text = np.asarray(ImageOps.invert(Image.open(text_name).convert("L")))
text_f = fft.fft2(text)
twidth = text.shape[1]
theight = text.shape[0]
letters_f = [0]*35
for i in range(35):
    letters_f[i] = fft.fft2(rot90(letters[i], 2), s=(theight, twidth))
letter_pos = []

def find_letters(letters_f, text_f, thres= 0.92):
    positions = []
    for let_f in letters_f:
        corr = abs(fft.ifft2(multiply(text_f, let_f)))
        max_corr = np.amax(corr)
        pos = []
        for i in range(corr.shape[0]):
            for j in range(corr.shape[1]):
                if corr[i, j] >= thres * max_corr:
                    pos.append((i, j))
        positions.append(pos)
        print(len(pos))
    return positions

def circle(text_name, positions, shape):
    new_img = np.array(Image.open(text_name).convert("RGB"))
    for pos in positions:
        i, j = pos
        for k in range(shape[0]):
            new_img[i - k, j] = (255, 0, 0)
            new_img[i - k, j - shape[1]] = (255, 0, 0)
        for l in range(shape[1]):
            new_img[i, j - l] = (255, 0, 0)
            new_img[i - shape[0], j - l] = (255, 0, 0)
    plt.imshow(new_img)
    plt.show()

positions = find_letters(letters_f, text_f)
circle(text_name, positions[0], letters[0].shape)
circle(text_name, positions[1], letters[0].shape)
circle(text_name, positions[2], letters[0].shape)
circle(text_name, positions[3], letters[0].shape)









