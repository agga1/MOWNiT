import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import norm, qr, inv
from time import perf_counter

def QR(A):
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
        st1 = perf_counter()
        Q, R = QR(A)
        st2 = perf_counter()
        q, r = np.linalg.qr(A)
        st3 = perf_counter()
        assert (np.allclose(A, np.dot(Q, R))), "A != QR"
        assert (np.allclose(abs(q), abs(Q))), "q != Q"
        assert (np.allclose(abs(r), abs(R))), "r != R"
        print(f"✓  my: {st2-st1}, numpy: {st3-st2}")

# test_1([3, 50, 100, 200, 500])

# generating 8x8 matrixes with different cond
def generate_Ms(count):
    i = 0
    Ms = []
    conds = []
    A = np.random.rand(8, 8)
    B = np.random.rand(8, 8)
    U, _ = qr(A)
    V, _ = qr(B)
    while i < count:
        S = np.zeros(A.shape[0])
        S[0] = 1.
        for j in range(1, A.shape[0]):
            S[j] = S[j-1]+(i*j)
        S = sorted(S, reverse=True)
        cond = S[0]/S[7]
        M = np.dot(U*S, V)
        Ms.append(M)
        conds.append(cond)
        i += 1
    return Ms, conds

def get_val(Ms):
    I = np.identity(Ms[0].shape[0])
    vals = []
    for A in Ms:
        Q, R = QR(A)
        val = norm(I - Q.transpose() @ Q)
        vals.append(val)
    return vals

Ms, conds = generate_Ms(100)
vals = get_val(Ms)
plt.plot(conds, vals, 'o')
plt.show()

# --- zad 2 --------

def solve_overdet(A, B):
    m, n = A.shape
    Q, R = np.linalg.qr(A, mode="complete")
    Q1 = Q[:, :n]
    R1 = R[:n, :n]
    X = inv(R1)@(Q1.T@B)
    print(X)
    return X
# solve equation
# f(x) = a0 + a1*x + a2*x^2
def solve_polyn_2(xs, ys):
    A = np.zeros((xs.shape[0], 3))
    A[:, 0] = 1
    A[:, 1] = xs
    A[:, 2] = xs*xs
    return solve_overdet(A, ys.reshape(-1, 1))

def f(a, x):
    return a[0, 0] + a[1, 0]*x + a[2, 0]*(x**2)

xs = np.array([x for x in range(-5, 6)])
ys = np.array([2,7,9,12,13,14,14,13,10,8,4])
X = solve_polyn_2(xs, ys)
plt.plot(xs, ys, 'o')
# approximate function
xs_approx = [x for x in np.arange(-6., 7., 0.2)]
ys_approx = [f(X, x) for x in xs_approx]
plt.plot(xs_approx, ys_approx)
plt.show()


