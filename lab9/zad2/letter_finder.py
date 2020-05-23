import numpy as np
import matplotlib.pyplot as plt
from zad2.parser import order
from numpy import fft, rot90, multiply
from PIL import Image

def to_lines(letter_order, letter_shape):
    # split into lines
    lines_by_pos = {} # key: x positions of lines, val: list of letters in the line
    for pos, letter in letter_order:
        key_match = None
        for key in lines_by_pos.keys():
            if abs(key-pos[0]) < letter_shape[0]//2:
                key_match = key
                break
        if key_match is not None:
            lines_by_pos[key_match].append((pos[1], letter))
        else:
            lines_by_pos[pos[0]] = [(pos[1], letter)]
    print(f"found { len(lines_by_pos)} lines: ")
    lines_ordered = []
    for key, line in lines_by_pos.items():
        letter_order = sorted(line)
        line_str = ""+order[letter_order[0][1]]
        for i in range(1, len(letter_order)):
            if letter_order[i][0] - letter_order[i - 1][0] > letter_shape[1] + 3:
                line_str += " "
            line_str += order[letter_order[i][1]]
        lines_ordered.append((key, line_str))
    lines_ordered = list(map(lambda x: x[1] , sorted(lines_ordered)))
    for line in lines_ordered:
        print(line)
    return lines_ordered


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

# consolas150 # 2 5 7 2
# cn150 2 1 3 2
# text_name = "../res/courier_new_t2.png"
# alphabet_name = "../res/courier_new.png"
# alphabet = parse_alphabet(alphabet_name, 2, 1, 9, 7) #  courier new
# find_all_letters(text_name, alphabet)

# alphabet = parse_alphabet(alphabet_name, 2, 5, 7, 2)

