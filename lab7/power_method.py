from typing import Callable, Tuple

import numpy as np
from scipy.linalg import eigh, lu_factor, lu_solve, inv
import matplotlib.pyplot as plt
from time_eval import time_eval


def power_method(A: np.array, max_iter: int = 100000, eps: float = 1e-8, return_iter=False):
    """
    given a diagonalizable matrix A, the algorithm finds a number λ,
    which is the greatest (in absolute value) eigenvalue of A,
    and v - a corresponding (nonzero) eigenvector of λ.
    :param max_iter: algorithm stops at max_iter, or
    :param eps: after reaching ||xi−xi+1||< eps
    :param return_iter: returns nr of iterations as third element
    :return λ, v [,iter]
    """
    x = np.random.rand(A.shape[0])
    i = 0
    while i < max_iter:
        i += 1
        x2 = A @ x
        x2 /= np.linalg.norm(x2)  # normalize
        if np.linalg.norm(x2 - x) < eps or i+1==max_iter:
            break
        x = x2

    eig = x@A@x/(x@x)
    x /= np.linalg.norm(x, axis=0)

    if return_iter:
        return eig, x, i
    return eig, x

def inv_power_method(A: np.array, mu, max_iter: int = 100000, eps: float = 1e-8, return_iter=False):
    """ finding eigen vector using inverse power method, and eigenvalue using Rayleigh quotient
    :param A: matrix
    :param mu: approximation for the eigenvalue corresponding to the desired eigenvector
    :param max_iter: stop algorithm after @max_iter iterations
    :param eps: stop algorithm after reaching desired accuracy
    :param return_iter: returns nr of iterations as third element
    :return: λ, v [,iter]
    """
    v0 = np.identity(A.shape[0])[0]
    v, i = 0, 0
    AuI = A - mu * np.identity(A.shape[0])
    lupiv = lu_factor(AuI)
    while i< max_iter:
        i += 1
        v = v0
        w = lu_solve(lupiv, v)
        v = w / np.linalg.norm(w)
        if np.linalg.norm(v-v0) < eps or np.linalg.norm(v + v0) < eps:
            break
        mu = v.T @ A @ v
        v0 = v

    if return_iter:
        return mu, v, i
    return mu, v

def rayleigh_iteration(A: np.array, mu, max_iter: int = 100000, eps: float = 1e-8, return_iter=False):
    """ finding eigen vector using inverse power method, and eigenvalue using Rayleigh quotient
        :param A: matrix
        :param mu: approximation for the eigenvalue corresponding to the desired eigenvector
        :param max_iter: stop algorithm after @max_iter iterations
        :param eps: stop algorithm after reaching desired accuracy
        :param return_iter: returns nr of iterations as third element
        :return: λ, v [,iter]
        """
    v = np.random.rand(A.shape[0])
    i = 0
    while i < max_iter:
        i += 1
        AuI = A - mu * np.identity(A.shape[0])
        w = inv(AuI)@v
        w = w / np.linalg.norm(w)
        mu = (w.T @ A @ w )/(w.T@w)
        if np.linalg.norm(v - w) < eps or np.linalg.norm(v + w) < eps:
            break
        v = w

    if return_iter:
        return mu, v, i
    return mu, v

def check_with_library(n, func: Callable[[np.array, any], Tuple[float, np.array]], eps=1e-5):
    A = np.random.rand(n, n)
    A = A.T @ A
    _ , [eig, v] = time_eval(func, "My power method", 1, A)

    _, [eig_lib, v_lib] = time_eval(eigh, "Library function", 1, A, eigvals=(n - 1, n - 1))
    eig_lib, v_lib = eig_lib[0], np.transpose(v_lib)[0]

    if abs(eig_lib - eig) > eps:
        print("wrong eigen value")
        return

    for idx in range(len(v)):
        if abs(abs(v[idx]) - abs(v_lib[idx])) > eps:
            print("wrong eigen vector")
            return
    print("Algorithm correct!\n")


def plot_power_method():
    """ plots correlation between time needed for power_method execution and input matrix size"""
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

# checking power_method correctness using library functions
check_with_library(100, power_method, 1e-5)
check_with_library(300, power_method, 1e-5)

# plotting correlation between time needed for power_method execution and input matrix size
plot_power_method()

# comparing results
A = np.random.rand(10, 10)
A = A * np.transpose(A)

def print_summary(name, func, *args, **kwargs):
    print(f"{name}:")
    eigvec, eigval , iter = func(*args, **kwargs)
    print("value: ", round(eigvec, 8), "iterations:", iter, "\n")


print_summary("power method", power_method, A, 1000, 1e-8, return_iter=True)
print_summary("inverse method, random sigma", inv_power_method, A, 10, 1000, 1e-8, return_iter=True)
print_summary("inverse method, other random sigma", inv_power_method, A, 100, 1000, 1e-8, return_iter=True)
mu, _ = power_method(A, max_iter=10, eps=0.3)  # assuming we know a good approximation of eigenvalue
print_summary("inverse method, having good approximation", inv_power_method, A, mu, 1000, 1e-8, return_iter=True)
print_summary("rayleigh method", rayleigh_iteration, A, mu, 1000, 1e-8, return_iter=True)

print("rayleigh method converges the quickest")

