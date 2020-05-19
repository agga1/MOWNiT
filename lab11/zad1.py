import matplotlib.pyplot as plt
import numpy as np
from numpy import diag
from numpy.linalg import norm, qr, svd, inv
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

test_1([3, 50, 200])

# generating 8x8 matrixes with different cond
I = np.identity(8)
cond_to_val = dict()
while len(cond_to_val) < 50:
    A = np.random.rand(8, 8)
    U, S, Vt = svd(A)
    cond = S[0] / S[7]
    if cond not in cond_to_val:
        Q, R = graham_schmidt(A)
        val = norm(I - Q.transpose() @ Q)
        cond_to_val[cond] = val

to_print = list(cond_to_val.items())
to_print.sort()
xs = [pair[0] for pair in to_print]
ys = [pair[1] for pair in to_print]
plt.plot(xs, ys, 'o')
# plt.show()

# ||I-Q^T*Q|| (cond(A))

# prepare A matrix
A = np.zeros((5, 3))
A[:, 0] = 1
A[0, 1] = 1
A[1, 2] = 1

B = np.matrix([3, 4, 1, 1, 1]).reshape(-1,1)

def solve_overdet(A, B):
    m, n = A.shape
    Q, R = np.linalg.qr(A, mode="complete")
    Q1 = Q[:, :n]
    R1 = R[:n, :n]
    X = inv(R1)@(Q1.T@B)
    print(X)
    return X

result = solve_overdet(A, B)

