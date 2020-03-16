import math
import decimal as dec
from typing import List, Callable, Tuple

max_iter = 100000

def newton(fder: Callable, f: Callable, prec: int, span: List, eps: float, max_iter=max_iter)  -> Tuple[dec.Decimal, int]:
    if fder is None:
        raise Exception("derivative not given")

    dec.getcontext().prec = prec
    a, b = span

    x = dec.Decimal(a)
    next = x - f(x) / fder(x)

    nr_iter = 1
    while (not math.isclose(abs(next-x), 0, abs_tol=eps)) and (nr_iter < max_iter):
        x = next
        next = x - f(x) / fder(x)

        nr_iter += 1

    if nr_iter == max_iter:
        print("maximum number of iterations reached")
        return x, nr_iter

    return x, nr_iter
