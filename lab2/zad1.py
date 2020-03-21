import numpy as np
from time_eval import time_eval


def gauss_jordan(m: np.array, eps = 1.0/(10**10)):
    (h, w) = (m.shape[0], m.shape[1])
    for y in range(0, h):
        pivot = y
        for candidate in range(y+1, h):    # Finding max pivot
            if abs(m[candidate][y]) > abs(m[pivot][y]):
                pivot = candidate
        m[[y, pivot]] = m[[pivot, y]]
        if abs(m[y][y]) <= eps:     # Singular?
            return False
        for row in range(y+1, h):    # Eliminate column y
            factor = m[row][y] / m[y][y]
            m[row, y:] -= m[y,y:]*factor
    for y in range(1, h):
        for row in range(0, y):
            factor = m[row][y]/m[y][y]
            m[row, y:] -= m[y, y:]*factor
    for row in range(0, h):
        m[row][-1] /= m[row][row]
    result = m[:, -1]
    return result


""" comparing above algorithm with numpy library function linalg.solve: """
for i in range(5):
    size =100*(i+4)
    print(f"\ncheck for A {size}x{size}")
    m = np.random.rand(size, size+1)
    m = 10 * m
    n = m.copy()
    time_eval(gauss_jordan, [m], "my jordan", 1, True, True)
    time_eval(np.linalg.solve, [n[:, :-1], n[:, -1]], "linalg.solve", 1, True, True)
