import matplotlib.pyplot as plt
import numpy as np


def logistic_map(r, x):
    return r * x * (1-x)


def plot_bifurcation(x_density, r_range, y_density, x):
    r = np.linspace(r_range[0], r_range[1], x_density)

    fig, ax = plt.subplots(1, 1)

    skip = 300
    for i in range(skip):
        x = logistic_map(r, x)

    for i in range(y_density):
        x = logistic_map(r, x)
        ax.plot(r, x, ',k', alpha=.25)

    ax.set_xlim(r_range[0], r_range[1])
    ax.set_title("Bifurcation diagram")
    plt.xlabel("r")
    plt.ylabel("Xn")


def iterate_xn_float(x, r, n):
    x = np.float32(x)
    r = np.float32(r)
    xs = [np.float32(i) for i in range(n)]
    ys = []
    for i in range(n):
        x = np.float32(logistic_map(r, x))
        ys.append(x)

    return xs, ys

def iterate_xn_double(x, r, n):
    x = np.float64(x)
    r = np.float64(r)
    xs = [np.float64(i) for i in range(n)]
    ys = []
    for i in range(n):
        x = np.float64(logistic_map(r, x))
        ys.append(x)

    return xs, ys
def plot_trajectories(x, r, n):
    fig, ax = plt.subplots(1, 1)

    Ox, Oy = iterate_xn_float(x, r, n)
    plt.plot(Ox, Oy, c="blue")

    Ox, Oy = iterate_xn_double(x, r, n)
    plt.plot(Ox, Oy, c="red")

    ax.set_xlim(0, n)
    ax.set_title("trajectories comparison")
    plt.xlabel("n")
    plt.ylabel("xn")
    plt.savefig('trajectories.png', dpi=800)

# count iterations to zero
def iter_to_zero(x, r=np.float32(4.0)):
    x = np.float32(x)

    it = 0
    while x > 0 and it < 10000:
        it += 1
        x = np.float32(logistic_map(r, x))

    return it


def run_iter_to_zero():
    for x in np.linspace(0, 1, num=50):
        print("for x0 = ",x, " iter= ",iter_to_zero(x),"\n")


def main_func():

    plot_bifurcation(2000, (1, 4), 100, 0.6)
    plot_trajectories(0.1, 3.75, 100)
    run_iter_to_zero()


main_func()
