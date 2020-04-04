from random import randint
import numpy as np

def nextStateRnd(bim):
    n = bim.shape[0]
    x1 = randint(0, n - 1)
    y1 = randint(0, n - 1)

    x2 = randint(0, n - 1)
    y2 = randint(0, n - 1)

    while x1==x2 and y1==y2:
        x2 = randint(0, n - 1)
        y2 = randint(0, n - 1)

    res = np.copy(bim)
    res[x1, y1] = bim[x2, y2]
    res[x2, y2] = bim[x1, y1]

    return res, [[x1, y1], [x2, y2]]

def nextStateNeigh(bim):
    n = bim.shape[0]
    while(True):
        x1 = randint(0, n - 1)
        y1 = randint(0, n - 1)
        x2Opt = [x1+1, x1, x1-1, x1]
        y2Opt = [y1, y1+1, y1, y1-1]
        OptIdx = randint(0, 3)
        x2 = x2Opt[OptIdx]%n
        y2 = y2Opt[OptIdx]%n
        if bim[x1, y1] != bim[x2, y2]:
            break

    res = np.copy(bim)
    res[x1, y1] = bim[x2, y2]
    res[x2, y2] = bim[x1, y1]
    return res, [[x1, y1], [x2, y2]]
