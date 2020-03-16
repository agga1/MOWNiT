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
    dec.getcontext().prec = prec

    if f(a) * f(b) > 0:
        raise Exception("same sign at both ends!")

    asc = True  # f(a)<0 and f(b)>0
    if f(a) > f(b):
        asc = False  # f(a)>0 and f(b)<0

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

