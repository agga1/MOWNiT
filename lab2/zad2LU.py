import numpy as np

def AtoLU(A: np.array):
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
            U[row, y:] -= U[y, y:] * factor
            L[row][y] = factor
    return P.transpose()@L, U


def checkALU(A, L, U, eps = 1e-10):
    Check = abs(A - L@U) <eps
    return np.all(Check)


def factorizeAndCheck(n: int, printLU=True):
    """
    prints L, U and if LU factorization of nxn matrix is correct
    """
    A = np.random.rand(n, n)
    A = 10 * A

    L, U =AtoLU(A)
    if printLU:
        np.set_printoptions(precision=6, suppress=True)
        print("L:\n", L)
        print("U:\n",U)
    ok = checkALU(A, L, U)
    print("correct" if ok else "incorrect")

factorizeAndCheck(6)
factorizeAndCheck(100, False)
factorizeAndCheck(200, False)
factorizeAndCheck(300, False)

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

""" check with scipy """
# A = np.random.rand(10, 10)
# A = 10 * A
# P, L, U =linalg.lu(A)
# # print(L)
# # print(U)
# # print(P)
# print(P@L@U)
# print(A)
# print(P.dot(A))
