import numpy as np
from scipy import integrate
from time import perf_counter
from test_func import f1, f2, f3


def simpson(xs, ys):
    n = len(xs)
    h = (xs[-1] - xs[0])/n  # span
    integral = ys[0]+ys[-1]
    integral += 2*np.sum(ys[1:-1])

    mask = np.ones(ys.shape, dtype=bool)
    mask[::2] = 0
    integral += 2*np.sum(ys[mask])
    integral *= h/3
    return integral


def check_with_lib(span, n, f, title=None):
    step = (span[1]-span[0])/n
    xs = np.arange(span[0], span[1]+step, step)
    ys = f(xs)
    st1 = perf_counter()
    my_int = simpson(xs, ys)
    st2 = perf_counter()
    lib_int = integrate.simps(ys, xs)
    st3 = perf_counter()
    if title:
        print(title, n, "points")
    print("lib:",lib_int, "\ttime:", round(st3-st2, 6))
    print("my: ",my_int, "\ttime:", round(st2-st1, 6))
    print()

# na podstawie poniższych testów możemy stwierdzić, że metoda złożonego simpsona
# daje nam całkiem dobre przybliżenie w bardzo szybkim czasie (jest szybsza od funkcji bibliotecznych).

check_with_lib([1, 100], 100, f1, "f1")
check_with_lib([1, 100], 1000, f1, "f1")
check_with_lib([1, 100], 10000, f1, "f1")
check_with_lib([1, 100], 100000, f1, "f1")

check_with_lib([1, 100], 1000, f2, "f2")
check_with_lib([1, 100], 10000, f2, "f2")
check_with_lib([1, 100], 100000, f2, "f2")

check_with_lib([10, 15], 1000, f2, "f2")

check_with_lib([1, 100], 1000, f3, "f3")
check_with_lib([1, 100], 100000, f3, "f3")

