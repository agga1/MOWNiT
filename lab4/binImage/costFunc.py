import numpy as np
from energyFunctions import energyFuncStripes

def countPointEnergy(bim, r, c, neighNr, eFunc=energyFuncStripes):
    cost =0
    x = [-1, 0, 1, 0]  # 4 closest neighbours
    y = [0, 1, 0, -1]
    for i in range(4):
        cost += eFunc(bim, r, c, x[i], y[i], 1)
    if neighNr == 4:
        return cost
    x = [-1, 1, 1, -1]  # 8 closest neighbours
    y = [1, 1, -1, -1]
    for i in range(4):
        cost += eFunc(bim, r, c, x[i], y[i], np.sqrt(2))
    if neighNr == 8:
        return cost
    iter= [-2, -1, 0, 1, 2] # 16 neighbours
    for i in iter:
        cost += eFunc(bim, r, c, i, -2)
        cost += eFunc(bim, r, c, i, 2)
        if abs(i) != 2:
            cost += eFunc(bim, r, c, -2, i)
            cost += eFunc(bim, r, c, 2, i)
    return cost

def costFunc(bim, neighNr, energyFunc=energyFuncStripes, prevstate=None, changed=None):
    assert neighNr in [4, 8, 16], "only options: neighNr = 4, 8 or 16!"
    n = bim.shape[0]
    cost = 0.
    if prevstate is None:  # no previous results
        for r in range(n):
            for c in range(n):
               cost += countPointEnergy(bim, r, c, neighNr, energyFunc)
    else:
        cost = prevstate.cost
        for point in changed:
            cost -= countPointEnergy(prevstate.val, point[0], point[1], neighNr, energyFunc)
            cost += countPointEnergy(bim, point[0], point[1], neighNr, energyFunc)
    return cost



