from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

class Stats:
    def __init__(self, letters_in_order, text_name, letter_shape):
        self.order = letters_in_order
        self.occurences = [0]*len(self.order)
        self.lines = []  # list of lines as strings
        self.letters_pos_idx = None  # list of tuples ((x,y), letter_idx)

        self.text_name = text_name  # for visualization
        self.letter_shape = letter_shape

    def add_letters(self, letters_pos_idx):
        self.letters_pos_idx = letters_pos_idx
        self.count_occur()
        self.to_lines()


    def count_occur(self):
        """ occurences of letters sorted according to 'order' """
        for pos, idx in self.letters_pos_idx:
            self.occurences[idx] += 1

    def to_lines(self):
        """
        split list of letters given like ((x,y), idx) into lines
        """
        lines_by_pos = {}  # key: x positions of lines, val: list of letters in the line
        for pos, letter in self.letters_pos_idx:
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
            line_str = "" + self.order[letter_order[0][1]]
            for i in range(1, len(letter_order)):
                if letter_order[i][0] - letter_order[i - 1][0] > self.letter_shape[1] + 3:
                    line_str += " "
                line_str += self.order[letter_order[i][1]]
            lines_ordered.append((key, line_str))
        lines_ordered = list(map(lambda x: x[1], sorted(lines_ordered)))

        self.lines = lines_ordered

    def circle(self, lets, title=True):
        result = np.array(Image.open(self.text_name).convert("RGB"))
        h, w = self.letter_shape
        for pos, let_idx in self.letters_pos_idx:
            if let_idx not in lets:
                continue
            i, j = pos
            color = (255, 0, 0)
            result[i - h:i, j] = color
            result[i - h:i, j - w] = color
            result[i, j - w:j] = color
            result[i - h, j - w:j] = color
        plt.imshow(result)
        if title:
            plt.title(str([self.order[let] for let in lets]))
        plt.show()

    def print_text(self):
        for line in self.lines:
            print(line)

