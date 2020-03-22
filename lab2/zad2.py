import numpy as np


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
            U[row, y:] -= U[y, y:] * factor
            L[row][y] = factor
    return L, U, P.transpose()


def checkALUP(A, L, U, P, eps = 1e-10):
    Check = abs(A - P@L@U) <eps
    return np.all(Check)


def factorizeAndCheck(n: int, printLU=True):
    """
    prints L, U and whether LU factorization of nxn matrix is correct
    """
    A = np.random.rand(n, n)
    A = 10 * A

    L, U, P =AtoLUP(A)
    if printLU:
        np.set_printoptions(precision=6, suppress=True)
        print("L:\n", L)
        print("U:\n",U)
    ok = checkALUP(A, L, U, P)
    print("correct" if ok else "incorrect")


factorizeAndCheck(6)
factorizeAndCheck(100, False)
factorizeAndCheck(200, False)
factorizeAndCheck(300, False)


