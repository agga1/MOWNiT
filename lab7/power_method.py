import numpy as np
from scipy.linalg import eigh, lu_factor, lu_solve
import matplotlib.pyplot as plt
from time_eval import time_eval

def power_method(A: np.array, max_iter: int = 100000, eps: float = 1e-8):
    """
    given a diagonalizable matrix A, the algorithm finds a number λ,
    which is the greatest (in absolute value) eigenvalue of A,
    and v - a corresponding (nonzero) eigenvector of λ.
    :param max_iter: algorithm stops at max_iter, or
    :param eps: after reaching ||xi−xi+1||< eps
    :return λ, v
    """
    x = np.random.rand(A.shape[0])
    for i in range(max_iter):
        x2 = A @ x
        x2 /= np.linalg.norm(x2)  # normalize
        if np.linalg.norm(x2 - x) < eps:
            print(f"{i} iter")
            break
        x = x2

    eig = x@A@x/(x@x)
    # eig = np.max(np.abs(x))
    return eig, x


def check(A, λ, v):
    print(A @ v)
    print(λ * v)


def check_with_library(n, func, eps=1e5):
    A = np.random.rand(n, n)
    A = A.T @ A
    _ , [eig, v] = time_eval(func, "My power method", 1, A)

    _, [eig_lib, v_lib] = time_eval(eigh, "Library function", 1, A, eigvals=(n - 1, n - 1))
    eig_lib, v_lib = eig_lib[0], np.transpose(v_lib)[0]

    if abs(eig_lib - eig) > eps:
        print("wrong eigen value")
        return
    for idx in range(len(v)):
        if abs(v[idx] - v_lib[idx]) > eps:
            print("wrong eigen vector")
            return
    print("Algorithm correct!\n")

def summary():
    xs = []
    ys = []
    for k in range(100, 2500, 100):
        A = np.random.rand(k, k)
        A = A * np.transpose(A)
        time, _ = time_eval(power_method, None, 10, A)  # average from 10 tries
        xs.append(k)
        ys.append(time)
    plt.plot(xs, ys)
    plt.show()

def inverse_power_iteration(A, u, max_iters, epsilon):
    v0 = np.identity(A.shape[0])[0]
    AuI = A - u*np.identity(A.shape[0])
    lupiv = lu_factor(AuI)
    for i in range(max_iters):
        v = v0
        w = lu_solve(lupiv, v)
        v = w / np.linalg.norm(w)
        if np.linalg.norm(v-v0) < epsilon or np.linalg.norm(v+v0) < epsilon:
            print(f"{i} iter")
            return u, v
        u = v.T @ A @ v
        v0 = v


A = np.random.rand(10, 10)
A = A * np.transpose(A)

# eigval, eigvec= inverse_power_iteration(A, 0, 100000, 1e-8)
# print(eigvec)
eigval, eigvec = power_method(A, 100000, 1e-8)
print(eigvec)

check_with_library(100, power_method, 1e5)
check_with_library(1000, power_method, 1e5)
# summary()


