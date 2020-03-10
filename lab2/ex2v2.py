"""
Ux=y
Ly=B
"""
import numpy as np


def AtoLU(m: np.array):
    m =np.array(m)
    assert m.shape[0] == m.shape[1]
    n = m.shape[0]
    U = [[0]]
    for y in range(0, n):
        pivot = y
        for candidate in range(y + 1, n):  # Finding max pivot
            if abs(m[candidate][y]) > abs(m[pivot][y]):
                pivot = candidate
        (m[y], m[pivot]) = (m[pivot], m[y])
        for row in range(y+1, n):    # Eliminate column y
            factor = m[row][y] / m[y][y]
            for el in range(y, n):
                m[row][el] -= m[y][el] * factor
            m[row][y] = factor
    print(m)


m=[[1.1, 2.2, 4.0, 2.0],[3.3, 4.4, 5.0, 1.0], [2.2, 4.4, 5.5, 6.6]]

A=[[1.1, 2.2, 4.0],[3.3, 4.4, 5.0], [2.2, 4.4, 5.5]]
B=[2.0, 1.0, 6.6]

# m=[[1.0, 0, 0, 0],[0, 1.0, 0, 1.0], [2.2, 4.4, 5.5, 6.6]]
AtoLU(A)
