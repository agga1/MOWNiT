from test_func import f4, f5, f1, f6
from scipy import integrate
import numpy as np

def get_nodes(a, b, n):  # get evenly distributed points between a and b (inclusive)
    if b <= a:
        return None, 0
    h = (b - a) / n
    xs = np.arange(a, b+1e-11, h)
    return xs, h

def trapezoidal(ys, h):
    return h/2*(ys[0] + 2*np.sum(ys[1:-1]) + ys[-1])

def trapezoidal2d(f, xspan, xn, ymin, ymax, yn):
    xs, hx = get_nodes(xspan[0], xspan[1], xn)
    results = []
    for x in xs:
        ys, hy = get_nodes(ymin(x), ymax(x), yn)
        if ys is None:
            continue
        zs = f(x, ys)
        results.append(trapezoidal(zs, hy))
    results = np.array(results)
    return trapezoidal(results, hx)

def check(f, xmin, xmax, ymin, ymax, xnum, ynum, name):
    my_int = trapezoidal2d(f, [xmin, xmax], xnum, ymin, ymax, ynum)
    lib_int = integrate.dblquad(f, xmin, xmax, ymin, ymax)[0]
    print(f" {name} {xnum} xs, {ynum} ys")
    print("my:", my_int)
    print("lib:", lib_int, "\n")

# -----checking f5

# możemy zaobserwować szybkie zbieganie naszej implementacji metody trapezów do implementacji
# funkcji bibliotecznej. Już w okolicy siatki 100X100, błąd względny wynosi ok. 0.2%.
# dla siatki 1000X1000 wynosi on zaledwie 0.002%. Jest to bardzo dokładne przybliżenie, jak na
# szybkość działania metody.
check(f5, -3, 3, lambda x: -5, lambda x: 5, 10, 10, "f5")
check(f5, -3, 3, lambda x: -5, lambda x: 5, 100, 100, "f5")
check(f5, -3, 3, lambda x: -5, lambda x: 5, 1000, 1000, "f5")
check(f5, -3, 3, lambda x: -5, lambda x: 5, 10000, 10000, "f5")

# ------checking f4

# tutaj również dokładność poniżej 1% otrzymujemy bardzo szybko.
check(f4, 0, 1, lambda x: 0, lambda x: 1-x, 100, 100, "f4")
check(f4, 0, 1, lambda x: 0, lambda x: 1-x, 1000, 1000, "f4")
check(f4, 0, 1, lambda x: 0, lambda x: 1-x, 10000, 10000, "f4")
