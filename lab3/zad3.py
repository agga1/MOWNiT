import math
import decimal as dec
from typing import List, Callable, Tuple

max_iter = 100000

def secant(f: Callable, prec: int, span: List, eps: float, max_iter=max_iter) -> Tuple[dec.Decimal, int]:
    dec.getcontext().prec = prec
    a, b = span

    if f(a) * f(b) > 0:
        raise Exception("same sign at both ends!")

    x = [0] * 3
    x[0] = dec.Decimal(a)
    x[1] = dec.Decimal(b)

    nr_iter = 0
    while (not math.isclose(x[1] - x[0], 0, abs_tol=eps)) and (nr_iter < max_iter) and (
            not math.isclose(f(x[1]) - f(x[0]), 0, abs_tol=eps)):
        # if()
        x[2] = (f(x[1]) * x[0] - f(x[0]) * x[1]) / (f(x[1]) - f(x[0]))
        x[2] = dec.Decimal(x[2])
        x[0] = x[1]
        x[1] = x[2]
        nr_iter += 1

    x = dec.Decimal(x[2])

    if nr_iter == max_iter:
        print("maximum number of iterations reached")
        return x, nr_iter

    return x, nr_iter
