import numpy as np
from numpy.linalg import inv
from scipy import linalg


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
        L[[y, pivot]] = L[[pivot, y]]

        L[y][y] = 1
        for row in range(y+1, n):    # Eliminate column y
            factor = U[row][y] / U[y][y]
            for el in range(y, n):
                U[row][el] -= U[y][el] * factor
            L[row][y] = factor
    return L, U, P.transpose()


def checkALUP(A, L, U, P):
    print(L.dot(U))
    print(P.dot(A))
    # checkEquals(L.dot(U), P.dot(A))


def checkEquals(A, B):
    print(A==B)
size = 5
A = np.random.rand(size, size)
A = 10 * A

# L, U, P =AtoLUP(A)
# print(L)
# print(U)
# print(P)
P, L, U =linalg.lu(A)
# print(L)
# print(U)
# print(P)
print(P@L@U)
print(A)
# print(P.dot(A))

# L, U, P =AtoLUP(A)
# checkALUP(A, L, U, P)

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
