import numpy as np
from PIL import Image
from PIL import ImageOps
from math import trunc
import matplotlib.pyplot as plt

order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         ',', '.', '?', '!', ':', ';', '-']

def parse_alphabet(filename, up=2, down=1, left=3,right=2):
    alphabet = np.asarray(ImageOps.invert(Image.open(filename).convert("L")))
    alphabet = alphabet[up:-down, left:-right]
    # print(alphabet.shape)
    return alphabet

def parse_text(text_name):
    return np.asarray(ImageOps.invert(Image.open(text_name).convert("L")))

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
    # print(letters[0].shape)
    return letters












