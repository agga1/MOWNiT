import math
import decimal as dec
import numpy as np
from typing import List, Callable

from testFunc import f4, f1

max_iter = 100000


def bisection(f: Callable, prec: int, span: List, eps):
    """
    :param prec: minimum nr of significant numbers
    :param span: [a, b]
    :param eps: absolute error of result
    :return: x, where f(x)-0 < eps
    """
    a, b = span

    if f(a) * f(b) > 0:
        print("same sign at both ends!")
        return

    asc = True  # f(a)<0 and f(b)>0
    if f(a) > f(b):
        asc = False  # f(a)>0 and f(b)<0

    dec.getcontext().prec = prec
    error = dec.Decimal(b) - dec.Decimal(a)  # current [a,b] interval length
    iter_nr = 0
    while not (math.isclose(error, 0, abs_tol=eps) or iter_nr > max_iter):
        error = dec.Decimal(b) - dec.Decimal(a)
        error = error / 2
        mid_x = dec.Decimal(a) + error
        mid = f(mid_x)
        if (mid > 0 and asc) or (mid < 0 and not asc):
            b = mid_x
        else:
            a = mid_x
        iter_nr += 1

    if iter_nr > max_iter:
        print(f"precision impossible to reach given {prec} digits precision")

    return dec.Decimal(a), iter_nr


def expected_iter(span, eps):
    a, b = span
    expected_iter = math.ceil(np.log((a + b) / eps) / np.log(2))
    return expected_iter


# res, iter, exp = bisection(f4,34, [1.1234567,4],  1e-33)
res, iter = bisection(f1, 50, [1.5 * math.pi, 2 * math.pi], 1e-33)
print(res, iter)

# print_func_res(bisection, f1, 50, [1.5 * math.pi, 2 * math.pi], 1e-33)
