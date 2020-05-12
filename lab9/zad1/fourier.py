import numpy as np
from numpy import fft, rot90
import matplotlib.pyplot as plt


def display_gray(array):
    plt.imshow(array, cmap="gray")
    plt.show()


def find_pattern(array: np.array, pattern: np.array, threshold: float):
    """
    finds correlation in frequency dimension between given pattern
    and array, then classifies points as fish or not,
    based on the threshold.
    :return: classification
    """
    array_f = fft.fft2(array)
    pattern_f = fft.fft2(rot90(pattern, 2), s=array.shape)

    corr = abs(fft.ifft2(array_f * pattern_f))  # pointwise multiplication

    max_corr = np.amax(corr)
    classification = (corr >= threshold * max_corr) * 1  # binary array

    return classification


def plot_fourier(array):
    array_f = fft.fft2(array)

    # plot absolutes (as log10 to see differences)
    school_abs_f = np.log10(np.abs(array_f)).astype(np.float64)
    display_gray(school_abs_f)

    # plot phases
    school_phase = np.angle(array_f)
    display_gray(school_phase)
