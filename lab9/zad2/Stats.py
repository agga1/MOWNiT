from bisect import bisect

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from numpy import rot90


class Stats:
    def __init__(self, all_letters, text_name, letter_shape):
        self.occurences = {}
        for let in all_letters:
            self.occurences[let] = 0
        self.lines = []  # list of lines as strings
        self.pos_letter = None  # list of tuples ((x,y), 'a')

        self.text_name = text_name  # for visualization
        self.letter_shape = letter_shape
        self.rotation = 0

    def add_letters(self, pos_letter):
        self.pos_letter = pos_letter
        self.count_occur()
        self.to_lines()


    def count_occur(self):
        """ creates dict of occurrences of each letter """
        for pos, let in self.pos_letter:
            self.occurences[let] += 1

    def to_lines(self):
        """ split list of letters given like ((x,y), 'a') into lines """

        lines_by_pos = {}  # key: x positions of lines, val: list of letters in the line
        for pos, letter in self.pos_letter:
            key_match = None
            for key in lines_by_pos.keys():
                if abs(key - pos[0]) < self.letter_shape[0] // 2:
                    key_match = key
                    break
            if key_match is not None:
                lines_by_pos[key_match].append((pos[1], letter))
            else:
                lines_by_pos[pos[0]] = [(pos[1], letter)]
        print(f"found {len(lines_by_pos)} lines: ")
        lines_ordered = []
        for key, line in lines_by_pos.items():
            letter_order = sorted(line)
            line_str = "" + letter_order[0][1]
            for i in range(1, len(letter_order)):
                if letter_order[i][0] - letter_order[i - 1][0] > self.letter_shape[1]*1.5:
                    line_str += " "
                line_str += letter_order[i][1]
            lines_ordered.append((key, line_str))
        # sort lines
        lines_ordered = list(map(lambda x: x[1], sorted(lines_ordered)))
        self.lines = lines_ordered

    def circle(self, letters, show_title=True):
        """ circle chosen letters """
        result = np.array(Image.open(self.text_name).convert("RGB"))
        result = rot90(result, self.rotation)
        h, w = self.letter_shape
        for pos, let in self.pos_letter:
            if let not in letters:
                continue
            i, j = pos
            color = (255, 0, 0)
            result[i - h:i, j] = color
            result[i - h:i, j - w] = color
            result[i, j - w:j] = color
            result[i - h, j - w:j] = color
        plt.imshow(result)
        if show_title:
            plt.title(str(letters))
        plt.show()

    def print_text(self):
        for line in self.lines:
            print(line)

    def compare(self, answer, show_diff = False):
        text = '\n'.join(self.lines)
        if show_diff:
            undetected = self.diff(list(answer), list(text))
        else:
            undetected = len(answer) - self.quick_lcs(list(answer), list(text))
        mism_percent = round(100.*undetected/len(answer), 3)
        print(f"{mism_percent}% symbols mismatched")
        return mism_percent

    def quick_lcs(self, x: list, y: list):
        ranges = []
        ranges.append(len(y))  # I_0 = [0..n]
        for i in range(len(x)):
            positions = [j for j, l in enumerate(y) if l == x[i]]
            positions.reverse()
            for p in positions:
                k = bisect(ranges, p)
                if (k == bisect(ranges, p - 1)):
                    if (k < len(ranges) - 1):
                        ranges[k] = p
                    else:
                        ranges[k:k] = [p]
        return len(ranges) - 1

    def lcs_matrix(self, a, b):
        """ lcs algorithm using dynamic programming, to recreate differences in a and b.
        Works on lists of any kind of data with '==' defined (chars, tokens, classes) """
        mx = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                mx[i][j] = 1 + mx[i - 1][j - 1] if ai == bj else max(mx[i][j - 1], mx[i - 1][j])
        return mx


    def diff(self, a, b):
        mx = self.lcs_matrix(a, b)
        l = 0
        r = 0
        lines = []
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 and j >= 0:
            if i < 0:
                lines.append(f">>> [{j}] {b[j]}")
                l +=1
                j -= 1
            elif j < 0:
                lines.append(f"<< [{i}] {a[i]}")
                r += 1
                i -= 1
            elif a[i] == b[j]:
                i, j = i - 1, j - 1
            elif mx[i][j - 1] >= mx[i - 1][j]:
                lines.append(f">>> [{j}] {b[j]}")
                l+=1
                j -= 1
            elif mx[i][j - 1] < mx[i - 1][j]:
                lines.append(f"<< [{i}] {a[i]}")
                r += 1
                i -= 1
        lines.reverse()
        for line in lines:
            print(line)
        return max(r,l)
