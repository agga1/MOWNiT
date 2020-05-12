import numpy as np
import matplotlib.pyplot as plt
from math import trunc
from zad2.parser import parse_alphabet, parse_letters, parse_text, order
from numpy import fft, rot90, multiply
from PIL import Image

def to_str(letter_order, letter_shape):
    letter_order = sorted(  # TODO better separate lines
        filter(lambda x: x[0][0] < 40, letter_order),
        key=lambda x: x[0][1])

    line = letter_order[0][1]
    for i in range(1, len(letter_order)):
        if letter_order[i][0][1] - letter_order[i - 1][0][1] > letter_shape[1] + 3:
            line += " "
        line += letter_order[i][1]
    print(line)
    return line


def find_letters(letters, text, thres= 0.94):
    def flipped_fourier(items, shape):
        items_f = [0] * len(items)
        for i in range(len(items)):
            items_f[i] = fft.fft2(rot90(items[i], 2), s=(shape[0], shape[1]))
        return items_f
    letters_f = flipped_fourier(letters, text.shape)
    text_f = fft.fft2(text)
    positions = {}
    for idx, let_f in enumerate(letters_f):
        corr = abs(fft.ifft2(multiply(text_f, let_f)))
        max_corr = np.amax(corr)
        for i in range(corr.shape[0]):
            for j in range(corr.shape[1]):
                if corr[i, j] >= thres * max_corr:
                    if positions.get((i,j)) == None:
                        positions[(i, j)] = (idx, corr[i, j])
                    elif positions[(i, j)][1] < corr[i, j]:
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
    result = np.array(Image.open(text_name).convert("RGB"))
    h, w = letter_shape
    for key, val in positions.items():
        if val[0] not in lets:
            continue
        i, j = key
        color = (255, 0, 0)
        result[i-h:i, j] = color
        result[i-h:i, j-w] = color
        result[i, j-w:j] = color
        result[i-h, j-w:j] = color
    plt.imshow(result)
    if title:
        plt.title(str([order[let] for let in lets]))
    plt.show()

def reduce_noise(matrix, k):
    U, S, V = np.linalg.svd(matrix, full_matrices=False)  # singular value decomposition
    smat = np.diag(S)
    smat[k:, k:] = 0
    print(U.shape, S.shape, V.shape, smat.shape)
    return np.dot(U, np.dot(smat, V))

def reduce_noise2(matrix, k):
    U, S, V = np.linalg.svd(matrix, full_matrices=True)  # singular value decomposition
    Uvcts = np.matrix(U[:, :k])  # first k-t singular vectors
    Svals = np.diag(S[:k])  # k first singular values
    Vvcts = np.matrix(V[:k, :])  # transposed k-th vct = k-th column
    return Uvcts * Svals * Vvcts

def find_all_letters(text_name, alphabet_name):
    alphabet = parse_alphabet(alphabet_name, 2, 5, 7, 2)
    letters = parse_letters(alphabet)
    text = parse_text(text_name)
    text = reduce_noise2(text, trunc(50))

    # perform fourier transform
    positions = find_letters(letters, text, thres=0.93)
    clean_duplicates(positions, letters[0].shape, margin=7)

    # for i in range(10, 25):
    #     circle(text_name, positions, letters[0].shape, [i])
    circle(text_name, positions, letters[0].shape, [i for i in range(35)], False)

    # display
    letter_order = []
    for pos, val in positions.items():
        letter_order.append((pos, order[val[0]]))

    to_str(letter_order, letters[0].shape)


# consolas150 # 2 5 7 2
# cn150 2 1 3 2
text_name = "../res/consolas150.png"

alphabet_name = "../res/consolas_alph.png"
find_all_letters(text_name, alphabet_name)