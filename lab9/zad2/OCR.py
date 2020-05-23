from math import trunc
from numpy import fft, rot90, multiply

from zad2.Stats import Stats
from zad2.parser import parse_alphabet, parse_letters, parse_text, order
import numpy as np

font = {"consolas": ("../res/consolas150.png", [7, 8, 9, 10]),
        "courier_new": ("../res/courier_new150.png", [8, 6, 9, 8]),
        "lucida": ("../res/lucida150.png", [8, 5, 7, 6])  # up down left right
        }
test_answer = "some monospaced text. isnt that amazing?\n" \
              "and yet another line. ok! here: is a more\n" \
              "complicated, one."


class OCR:
    def __init__(self, font_name):
        alphabet = parse_alphabet(font[font_name][0], *font[font_name][1])
        self.letters = parse_letters(alphabet)
        self.letter_shape = self.letters[0].shape

    def parse_text(self, text_name):
        """ finds letters in given text (list of tuples: ((x,y), 'a') )
            and return results as Stats object """
        stats = Stats(order, text_name, self.letter_shape)
        text = parse_text(text_name)
        text = self.reduce_noise2(text, trunc(50))

        # perform fourier transform
        letters_by_pos = self.find_letters( text, thres=0.9)
        self.clean_duplicates(letters_by_pos, margin=0.5)


        # map to tuples: ( (x, y) , 'a' )
        letter_order = list(map( lambda sth: (sth[0], order[sth[1][0]]), letters_by_pos.items()))
        stats.add_letters(letter_order)
        return stats


    def find_letters(self, text, thres=0.94):
        """ perform fourier transform on each letter and on the main text
            to get correlation between images.
            :returns dict (key: (x, y) val: (idx of letter in 'order', correlation) """

        def flipped_fourier(items, shape):
            items_f = [0] * len(items)
            for i in range(len(items)):
                items_f[i] = fft.fft2(rot90(items[i], 2), s=(shape[0], shape[1]))
            return items_f

        letters_f = flipped_fourier(self.letters, text.shape)
        text_f = fft.fft2(text)
        positions = {}
        for idx, let_f in enumerate(letters_f):
            corr = abs(fft.ifft2(multiply(text_f, let_f)))
            max_corr = np.amax(corr)
            for i in range(corr.shape[0]):
                for j in range(corr.shape[1]):
                    if corr[i, j] >= thres * max_corr:
                        if positions.get((i, j)) == None:
                            positions[(i, j)] = (idx, corr[i, j])
                        elif positions[(i, j)][1] < corr[i, j]:
                            positions[(i, j)] = (idx, corr[i, j])
        return positions

    def clean_duplicates(self, letters_by_pos, margin=0.7):
        """
        :param letters_by_pos: dict key: (x,y), val: (idx, corr)
        :param margin: how much letters can overlap
        """
        def collide(a, b, shape, margin= 0.7):
            return (abs(a[1] - b[1]) <= shape[1]*margin and
                    abs(a[0] - b[0]) <= shape[0]*margin)

        todel = set()
        for key, val in letters_by_pos.items():
            for key2, val2 in letters_by_pos.items():
                if key2 != key and collide(key, key2, self.letter_shape, margin):
                    lesser = key2 if val[1] > val2[1] else key
                    todel.add(lesser)
        for key in todel:
            letters_by_pos.pop(key, None)

    def reduce_noise(self, matrix, k):
        U, S, V = np.linalg.svd(matrix, full_matrices=False)  # singular value decomposition
        smat = np.diag(S)
        smat[k:, k:] = 0
        print(U.shape, S.shape, V.shape, smat.shape)
        return np.dot(U, np.dot(smat, V))

    def reduce_noise2(self, matrix, k):
        U, S, V = np.linalg.svd(matrix, full_matrices=True)  # singular value decomposition
        Uvcts = np.matrix(U[:, :k])  # first k-t singular vectors
        Svals = np.diag(S[:k])  # k first singular values
        Vvcts = np.matrix(V[:k, :])  # transposed k-th vct = k-th column
        return Uvcts * Svals * Vvcts


def check(mfont, text = None):
    text = text if text is not None else f"../res/{mfont}_t.png"
    print(f"{mfont} font:")
    ocr = OCR(mfont)
    stats = ocr.parse_text(text)
    stats.circle([let for let in order], False)
    stats.print_text()
    stats.show_diff(test_answer)
    print()

check("lucida")
check("courier_new")
check("consolas")
