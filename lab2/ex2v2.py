"""
Ux=y
Ly=B
"""
import numpy as np
import scipy as sp
from scipy import linalg

def AtoLUinPlace(m: np.array):
    if isinstance(m , list):
        m = np.array(m)
    assert m.shape[0] == m.shape[1]
    n = m.shape[0]
    for y in range(0, n):
        pivot = y
        for candidate in range(y + 1, n):  # Finding max pivot
            if abs(m[candidate][y]) > abs(m[pivot][y]):
                pivot = candidate
        m[[y, pivot]] = m[[pivot, y]]
        for row in range(y+1, n):    # Eliminate column y
            factor = m[row][y] / m[y][y]
            for el in range(y, n):
                m[row][el] -= m[y][el] * factor
            m[row][y] = factor
    return m

def AtoLUP(A: np.array):
    U = np.array(A)
    assert U.shape[0] == U.shape[1]
    n = U.shape[0]
    L = np.zeros(U.shape, dtype=float)  # U = A
    P = np.identity(n)

    for y in range(0, n):
        pivot = y
        for candidate in range(y + 1, n):  # Finding max pivot
            if abs(U[candidate][y]) > abs(U[pivot][y]):
                pivot = candidate
        U[[y, pivot]] = U[[pivot, y]]
        P[[y, pivot]] = P[[pivot, y]]
        L[y][y] = 1
        for row in range(y+1, n):    # Eliminate column y
            factor = U[row][y] / U[y][y]
            for el in range(y, n):
                U[row][el] -= U[y][el] * factor
            L[row][y] = factor
    return L, U, P.transpose()

def checkALU(A, L, U):
    print(L.dot(U))



m=[[1.1, 2.2, 4.0, 2.0],[3.3, 4.4, 5.0, 1.0], [2.2, 4.4, 5.5, 6.6]]

A=np.array([[1.1, 2.2, 4.0],[3.3, 4.4, 5.0], [2.2, 4.4, 5.5]])
B=[2.0, 1.0, 6.6]

# m=[[1.0, 0, 0, 0],[0, 1.0, 0, 1.0], [2.2, 4.4, 5.5, 6.6]]
L, U, P =AtoLUP(A)
print(L)
print(U)
print(P)
P, L, U =linalg.lu(A)
print(L)
print(U)
print(P)