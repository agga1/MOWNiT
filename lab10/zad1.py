import numpy as np

from time_eval import time_eval

""" O(n^2) an O(NlogN) fourier transform """

def F(n) -> np.array:
    def dzeta(i, j):
        return np.exp(-2.j*np.pi*i*j/n)
    return np.fromfunction(dzeta, (n, n))

def DFT(x: np.array):
    n = len(x)
    return F(n)@x

def IDFT(y):
    n = len(y)
    return np.conj(F(n) @ np.conj(y)) / n

def FFT(x):
    """ Cooley-Turkey algorithm exploiting symmetry of the problem"""
    n = len(x)
    assert (n & (n-1) == 0) and n != 0, "size must be power of 2"
    if n <= 16:  # to amortize the recursion
        return DFT(x)
    else:
        even = FFT(x[0::2])
        odd = FFT(x[1::2])
        X = np.exp(-2j * np.pi * np.arange(n) / n)
        return np.concatenate((even + X[:n // 2] * odd,
                               even + X[n // 2:] * odd))

# checking correctness
def check_size(size):
    print(f"check fourier transform for n={size}")
    x = np.random.random(size)
    ok1 = "✓" if np.allclose(DFT(x), np.fft.fft(x)) else "✘"
    ok2 = "✓" if np.allclose(FFT(x), np.fft.fft(x)) else "✘"
    print(f"DFT: {ok1}, FFT: {ok2}")

    time_eval(DFT, "simple DFT", 2, x)
    time_eval(FFT, "FFT", 10, x)
    time_eval(np.fft.fft, "numpy fft", 10, x)
    print()


check_size(512)
check_size(1024)
check_size(4096)



