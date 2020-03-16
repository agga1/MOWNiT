import math

from testFunc import f1, f2, f3
from zad1 import bisection
from zad2 import newton
from zad3 import secant


def print_func_res(method, *args):
    res, iter = method(*args)
    print("solution: ",res, "\n", iter, "iter")

def print_res(*args):
    print(f"____Bisection method:")
    print_func_res(bisection, *args)
    print(f"____Newton's method:")
    # print_func_res(newton, *args)
    print(f"____Secant method:")
    # print_func_res(secant, *args)
    pass

def summary(nr, f, span):
    print(f"\nComparing f{nr}:\n")
    print("1e-7 precision:")
    print_res(f, 9, span, 1e-8)
    print("1e-15 precision:")
    print_res(f, 16, span, 1e-15)
    print("1e-33 precision:")
    print_res(f, 34, span, 1e-33)

summary(1, f1, [1.5 * math.pi, 2 * math.pi])
summary(2, f2, [0, math.pi/2])
summary(3, f3, [1, 3])