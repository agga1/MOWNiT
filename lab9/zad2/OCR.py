from math import trunc
from numpy import fft, rot90, multiply

from zad2.Stats import Stats
from zad2.letter_finder import reduce_noise2, clean_duplicates, circle, to_lines
from zad2.parser import parse_alphabet, parse_letters, parse_text, order
import numpy as np

font = {"consolas": ("../res/courier_new.png", [2, 1, 9, 7]),
        "courier_new": ("../res/courier_new.png", [2, 1, 9, 7])
        }

class OCR:
    def __init__(self, font_name):
        alphabet = parse_alphabet(font[font_name][0], *font[font_name][1])
        self.letters = parse_letters(alphabet)
        self.letter_shape = self.letters[0].shape

    def parse_text(self, text_name):
        stats = Stats(order, text_name, self.letter_shape)
        text = parse_text(text_name)
        text = reduce_noise2(text, trunc(50))

        # perform fourier transform
        letters_by_pos = self.find_letters( text, thres=0.93)
        clean_duplicates(letters_by_pos, self.letter_shape, margin=7)
        circle(text_name, letters_by_pos, self.letter_shape, [i for i in range(len(order))], False)

        # map to tuples: ( (x, y) , letter_idx)
        letter_order = list(map( lambda sth: (sth[0], sth[1][0]), letters_by_pos.items()))
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







ocr = OCR("consolas")
stats = ocr.parse_text("../res/courier_new_t2.png")
stats.print_text()
stats.circle([0])