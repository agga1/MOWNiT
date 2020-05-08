from operator import itemgetter

from numpy import fft
from other_parse import parse_alphabet, parse_letters, parse_text, flipped_fourier, find_letters, clean_duplicates, circle, \
    order

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

def find_all_letters(text_name, alphabet_name):
    alphabet = parse_alphabet(alphabet_name, 2, 5, 7, 2)
    letters = parse_letters(alphabet)
    text = parse_text(text_name)

    # perform fourier transform
    letters_f = flipped_fourier(letters, text.shape)
    text_f = fft.fft2(text)
    print(letters[0].shape)
    positions = find_letters(letters_f, text_f, thres=0.93)
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
text_name = "res/consolas150.png"

alphabet_name = "res/consolas_alph.png"
find_all_letters(text_name, alphabet_name)