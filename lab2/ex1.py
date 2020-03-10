# do 23
import numpy as np
from typing import Callable, List
from time import perf_counter

def run_with_time_count(func, args: List, name: str):
    start = perf_counter()
    func(*args)
    end = perf_counter()
    print(name, " running time: ", end-start)

def gauss_jordan(m: np.array, eps = 1.0/(10**10)):
    if isinstance(m , list):
        m = np.array(m)
    (h, w) = (m.shape[0], m.shape[1])
    for y in range(0, h):
        pivot = y
        for candidate in range(y+1, h):    # Finding max pivot
            if abs(m[candidate][y]) > abs(m[pivot][y]):
                pivot = candidate
        m[[y, pivot]] = m[[pivot, y]]
        if abs(m[y][y]) <= eps:     # Singular?
            return False
        for row in range(y+1, h):    # Eliminate column y
            factor = m[row][y] / m[y][y]
            for el in range(y, w):
                m[row][el] -= m[y][el] * factor
    for y in range(1, h):
        for row in range(0, y):
            factor = m[row][y]/m[y][y]
            for el in range(y, w):
                m[row][el] -= m[y][el] * factor
    for row in range(0, h):
        m[row][-1] /= m[row][row]
        m[row][row] = 1
    result = m[:, w-1]
    return result


m=np.array([[1.1, 2.2, 4.0, 2.0],[3.3, 4.4, 5.0, 1.0], [2.2, 4.4, 5.5, 6.6]])

A=m[:, :-1]
B=m[:, -1]
print(np.linalg.solve(A, B))
print(gauss_jordan(m))

run_with_time_count(gauss_jordan, [m], "my jordan")
run_with_time_count(np.linalg.solve, [A, B], "library function")


"""
3.wystarczy albo kirch albo wezly
brakuje m-n+1 cyklow prostych networkx do cyklow
networkx -> get random graph
jet color map (prąd wysoki - czerwony niski -nieb
napisz skrypt sprawdzający sume napiec (czy 0)- czy poprawny alg
uklady rownan nadokreslone
"""