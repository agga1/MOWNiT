import numpy as np
import matplotlib.pyplot as plt
from zad1 import FFT

""" comparing static and non-static signals -
    after fourier transform of signals comprised of the same 
    input functions but distributed differently,
    peaks are observed at the same frequencies, regardless of signal type
    (static or non static). Fourier transform is therefore better suited
    for the analysis of static signals. """

n = 512
xs = np.arange(n)
freq = np.fft.fftfreq(n)  # sample frequencies

# 3 periodic functions with different frequencies
ys1 = np.sin(xs)
ys2 = np.sin(2.5*xs)
ys3 = np.sin(5*xs)

ys_static = ys1 + ys2 + ys3
ys_dyn = np.concatenate((ys1[:n//3], ys2[n//3:2*n//3], ys3[2*n//3:]))

plt.plot(xs, ys_static)
plt.show()
plt.plot(xs, ys_dyn)
plt.show()

def plot_complex(xs, ys, title):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle(title)
    ax1.plot(xs, ys.real)
    ax1.set_title("real")
    ax2.plot(xs, ys.imag)
    ax2.set_title("imaginary")
    plt.show()


ys_static_f = FFT(ys_static)
plot_complex(freq, ys_static_f, 'Static signal')
ys_dyn_f = FFT(ys_dyn)
plot_complex(freq, ys_dyn_f, 'Dynamic signal')
