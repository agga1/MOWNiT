import matplotlib.pyplot as plt
import numpy as np
from numpy import fft, rot90, multiply
from PIL import Image
from PIL import ImageOps

x = np.arange(256)
y = np.sin(x)
plt.plot(x, y)
plt.show()
n = 400
sp = np.fft.fft(y, n=n)
print(sp.shape)
freq = np.fft.fftfreq(n)
plt.plot(freq, np.abs(sp.real))
plt.show()
y2 = np.zeros(n)
y2[:256] = y
sp = np.fft.fft(y2, n=n)
print(sp.shape)
freq = np.fft.fftfreq(n)
plt.plot(freq, np.abs(sp.real))
plt.show()

# x1 = np.arange(9.0).reshape((3, 3))
# x2 = np.ones((3,3))
# x2[2, 1] = 2
# c =np.multiply(x1, x2)
# print(c)