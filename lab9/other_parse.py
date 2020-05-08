import matplotlib.pyplot as plt
import numpy as np
from numpy import fft, rot90, multiply
from PIL import Image
from PIL import ImageOps
from math import trunc
text_name = "res/cn150.png"
alphabet_name = "res/cn_sep_b.png"
order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def parse_alphabet(filename, up=2, down=1, left=3,right=2):
    alphabet = np.asarray(ImageOps.invert(Image.open(filename).convert("L")))
    alphabet = alphabet[up:-down, left:-right]
    print(alphabet.shape)
    return alphabet

def parse_letters(alphabet):
    """
    :param alphabet: alphabet (in order as in @order) with space between each character
    :return: cropped each letter of alphabet
    """
    lwidth_true = alphabet.shape[1] / (len(order)*2-1)  # true letter length
    lwidth = trunc(lwidth_true)  # unified int letter length
    letters = []
    for i in range(0, len(order)*2-1, 2):
        fr = trunc(lwidth_true * i)
        to = trunc(lwidth_true * (i + 1))
        a = alphabet[:, fr:to]
        if a.shape[1] > lwidth:
            a = a[:, 1:]
        letters.append(a)
        # plt.imshow(a, cmap="gray")
        # plt.show()
    return letters


def parse_text(text_name):
    return np.asarray(ImageOps.invert(Image.open(text_name).convert("L")))


def flipped_fourier(letters, shape):
    letters_f = [0] * len(letters)
    for i in range(len(letters)):
        letters_f[i] = fft.fft2(rot90(letters[i], 2), s=(shape[0], shape[1]))
    return letters_f


def find_letters(letters_f, text_f, thres= 0.94):
    positions = {}
    for idx, let_f in enumerate(letters_f):
        corr = abs(fft.ifft2(multiply(text_f, let_f)))
        max_corr = np.amax(corr)
        for i in range(corr.shape[0]):
            for j in range(corr.shape[1]):
                if corr[i, j] >= thres * max_corr:
                    # print(f"found {order[idx]} at pos {i},{j}, corr {corr[i,j]}")
                    if positions.get((i,j)) == None:
                        # print(f"{i, j} not found")
                        positions[(i, j)] = (idx, corr[i, j])
                    elif positions[(i, j)][1] < corr[i, j]:
                        # print(f"found better, {positions[(i, j)][0]}->{idx}")
                        positions[(i, j)] = (idx, corr[i, j])
    return positions


def clean_duplicates(positions, shape, margin=4):
    def collide(a, b, shape, margin):
        return (abs(a[1] - b[1]) <= shape[1] - margin and
                abs(a[0] - b[0]) <= shape[0] - margin)
    todel = set()
    for key, val in positions.items():
        for key2, val2 in positions.items():
            if key2 != key and collide(key, key2, shape, margin):
                lesser = key2 if val[1] > val2[1] else key
                todel.add(lesser)
    for key in todel:
        positions.pop(key, None)


def circle(text_name, positions, letter_shape, lets, title=True):
    new_img = np.array(Image.open(text_name).convert("RGB"))
    for key, val in positions.items():
        if val[0] not in lets:
            continue
        i, j = key
        color = (255, 0, 0)
        for k in range(letter_shape[0]):
            new_img[i - k, j] = color
            new_img[i - k, j - letter_shape[1]] = color
        for l in range(letter_shape[1]):
            new_img[i, j - l] = color
            new_img[i - letter_shape[0], j - l] = color
    plt.imshow(new_img)
    if title:
        plt.title(str([order[let] for let in lets]))
    plt.show()










