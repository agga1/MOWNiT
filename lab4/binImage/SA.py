from math import exp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from OptimState import OptimState
from random import random

from costFunc import costFunc


def SAforBinImage(energyF, x, nextState, neighNr=4, iter=5000, T=100., show=100):
    alpha = 0.97
    state = OptimState(x, costFunc(x, neighNr, energyF))
    costs = [state.cost]
    for i in range(iter):
        newX, changedPts = nextState(state.val)
        newState = OptimState(newX, costFunc(newX, neighNr, energyF, state, changedPts) ) # , state, changedPts

        # decide whether change state
        delta = newState.cost - state.cost
        if delta >= 0:
            state.val = newState.val
            state.cost = newState.cost
        else:
            P =0 if newState.cost==0 else exp((delta/newState.cost) / T)
            if random() <= P:
                state = newState

        T = T*alpha
        costs.append(state.cost)
        if (i %show == 0): #i % show ==0
            print(state.cost)
    return state



