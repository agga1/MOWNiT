import matplotlib.pyplot as plt
import numpy as np
from numpy import diag
from numpy.linalg import norm, qr, svd
import time


def graham_schmidt(A):
    Q = np.copy(A)
    R = np.zeros(A.shape, dtype=float)

    # u1
    Q[:, 0] /= norm(Q[:, 0])

    # u2, ... uN
    for k in range(1, A.shape[1]):
        for i in range(k):
            Q[:, k] -= np.dot(Q[:, i], A[:, k]) * Q[:, i]

        Q[:, k] /= norm(Q[:, k])

    for i in range(A.shape[0]):
        for j in range(i+1):
            R[j, i] = np.dot(Q[:, j], A[:, i])

    return Q, R

def rnd_ortogonal(n):
    A = np.random.rand(n, n)
    A = A@A.T
    return A*10

def rnd(n):
    return np.random.rand(n, n)*10

def test_1(ns):
    for n in ns:
        print(f"test for n={n}")
        A = rnd(n)
        Q, R = graham_schmidt(A)
        q, r = np.linalg.qr(A)
        assert (np.allclose(A, np.dot(Q, R))), "A != QR"
        assert (np.allclose(abs(q), abs(Q))), "q != Q"
        assert (np.allclose(abs(r), abs(R))), "r != R"
        print("✓")

test_1([3, 50, 200, 500])

