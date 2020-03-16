import math
import decimal as dec

def f1(x):
    return dec.Decimal(math.cos(x) * math.cosh(x)) - 1


def f1der(x):
    return dec.Decimal(math.cos(x) * math.sinh(x) - math.sin(x) * math.cosh(x))


def f2(x):
    if math.isclose(x, 0.0, abs_tol=1e-9):
        return dec.Decimal(10000000)
    return dec.Decimal(1/x) - dec.Decimal(math.tan(x))


def f2der(x):
    if math.isclose(x, 0.0, abs_tol=1e-9):
        return dec.Decimal(-10000000)
    return dec.Decimal(-1/x**2) - dec.Decimal(1 / math.cos(x)**2)


def f3(x):
    return dec.Decimal(math.pow(2, -x) + math.pow(math.e, x) + 2*math.cos(x)) - 6


def f3der(x):
    return dec.Decimal(math.pow(math.e, x) - math.pow(2, -x) * math.log(2, math.e) - 2 * math.sin(x))
