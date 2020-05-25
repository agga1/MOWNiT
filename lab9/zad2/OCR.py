from math import trunc
from numpy import fft, rot90, multiply
from time import perf_counter
from zad2.Stats import Stats
from zad2.parser import parse_alphabet, parse_letters, parse_text, order
import numpy as np
import concurrent.futures
import matplotlib.pyplot as plt

font = {"consolas": ("../res/consolas150.png", [6, 8, 9, 5]),
        "courier_new": ("../res/courier_new150.png", [8, 7, 10, 5]),
        "lucida": ("../res/lucida150.png", [2, 1, 6, 3])

        }
test_short = "some monospaced text. isnt that amazing?\n" \
              "and yet another line. ok! here: is a more\n" \
              "complicated, one."

test2 = "the correlation operation in 2d is very straight-forward. we just take a filter of a given\n" \
        "size and place it over a local region in the image having the same size as the filter. we\n" \
        "continue this operation shifting the same filter through the entire image. this also helps us\n" \
        "achieve two very popular properties :\n" \
        "translational invariance: our vision system should be to sense, respond or detect the\n" \
        "same object regardless of where it appears in the image.\n" \
        "locality: our vision system focusses on the local regions, without regard to what else is\n" \
        "happening in other parts of the image."


class OCR:
    def __init__(self, font_name):
        alphabet = parse_alphabet(font[font_name][0], *font[font_name][1])
        self.letters = parse_letters(alphabet)
        self.letter_shape = self.letters[0].shape

    def parse_text(self, text_name):
        """ finds letters in given text (list of tuples: ((x,y), 'a') )
            and return results as Stats object """
        stats = Stats(order, text_name, self.letter_shape)
        st1 = perf_counter()
        text = parse_text(text_name)
        st11 = perf_counter()
        k = min(text.shape[0]//3, text.shape[1]//3)
        text = self.reduce_noise(text, k)
        st12 = perf_counter()
        print("svd: ", st12-st11)

        # perform fourier transform
        pos_idx_corr, stats.rotation = self.find_letters( text, thres=0.916)
        st13 = perf_counter()
        print("find letters time: ", st13-st12)
        pos_idx_corr = self.clean_duplicates(pos_idx_corr, margin=0.5)
        # map to tuples: ( (x, y) , 'a' )
        letter_order = list(map(lambda sth: (sth[0], order[sth[1]]), pos_idx_corr))
        st2 = perf_counter()
        print("deleting duplicates time:", st2-st13)
        print("whole ocr time: ", st2-st1)
        stats.add_letters(letter_order)
        return stats


    def find_letters(self, text, thres=0.94):
        """ perform fourier transform on each letter and on the main text
            to get correlation between images.
            :returns dict (key: (x, y) val: (idx of letter in 'order', correlation) """

        def flipped_fourier(items, shape):
            executor = concurrent.futures.ThreadPoolExecutor(max_workers=8)
            items_f = list(executor.map(lambda item: fft.fft2(rot90(item, 2), s=shape), items))
            return items_f
        rot = self.get_text_rotation(text)
        print("detected rotation:", rot)
        text_f = fft.fft2(rot90(text, rot))
        letters_f = flipped_fourier(self.letters, text_f.shape)
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        positions = list(executor.map(lambda x: self.correlation(x[0], x[1], text_f, thres), enumerate(letters_f)))
        positions = [y for x in positions for y in x]
        return positions, rot

    def get_text_rotation(self, text):
        text_f = fft.fft2(text)
        e_f = fft.fft2(rot90(self.letters[4], 2), s=text_f.shape)
        corr = abs(fft.ifft2(multiply(text_f, e_f)))
        best = 0
        best_corr = np.amax(corr)
        for i in range(1, 4):
            text_f = fft.fft2(rot90(text, i))
            e_f = fft.fft2(rot90(self.letters[4], 2), s=text_f.shape)
            corr = abs(fft.ifft2(multiply(text_f, e_f)))
            max_corr = np.amax(corr)
            if max_corr > best_corr:
                best = i
                best_corr = max_corr
        return best

    def correlation(self, idx, let_f, text_f, thres):
        positions = []
        corr = abs(fft.ifft2(multiply(text_f, let_f)))
        max_corr = np.amax(corr)
        for i in range(corr.shape[0]):
            for j in range(corr.shape[1]):
                if corr[i, j] >= thres * max_corr:
                    positions.append(((i, j), idx, corr[i, j]))
        return positions

    def clean_duplicates(self, pos_idx_corr, margin=0.7):
        """
        :param pos_idx_corr: list of tuples: ((x,y), idx, corr)
        :param margin: how much letters can overlap
        """
        def collide(a, b, shape, margin= 0.7):
            return (abs(a[1] - b[1]) <= shape[1]*margin and
                    abs(a[0] - b[0]) <= shape[0]*margin)
        filtered = []
        # print(len(pos_idx_corr))
        for pos, idx, corr in pos_idx_corr:
            i = 0
            too_little = False
            while i < len(filtered):
                if collide(filtered[i][0], pos, self.letter_shape, margin):
                    if filtered[i][2] < corr:
                        filtered.pop(i)
                    else:
                        too_little = True
                i += 1
            if not too_little:
                filtered.append((pos, idx, corr))
        return filtered

    def reduce_noise(self, matrix, k):
        U, S, V = np.linalg.svd(matrix, full_matrices=False)  # singular value decomposition
        smat = np.diag(S)
        smat[k:, k:] = 0
        return np.dot(U, np.dot(smat, V))


def check(mfont, text = None, test_answer =None, print_occ=False):
    text = text if text is not None else f"../res/{mfont}_t.png"
    print(f"{mfont} font:")
    ocr = OCR(mfont)
    stats = ocr.parse_text(text)
    stats.circle([let for let in order], False)
    stats.print_text()
    if test_answer is not None:
        stats.compare(test_answer, True)
    if print_occ:
        print(stats.occurences)
    print()

# klasyczne testy
check("courier_new", test_answer=test_short)
check("consolas", test_answer=test_short)
check("lucida", test_answer=test_short)

# 16 linijek tekstu
check("lucida", "../res/lucida_vlong.png", test2+"\n"+test2)

# testy obrotów
check("lucida",  "../res/lucida_t.png", test_short)
check("lucida",  "../res/lucida_inv.png", test_short)
check("lucida",  "../res/lr1.png", test_short)
#
check("lucida", test_answer=test_short, print_occ=True)
