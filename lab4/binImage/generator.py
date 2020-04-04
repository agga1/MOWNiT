import numpy as np
from random import random

def createBinImage(n: int, d:float):
    """ create new binary image nxn, with dark point density d"""
    bim = np.zeros((n, n))
    for r in range(n):
        for c in range(n):
            if random() < d:
                bim[r, c] = 1
    return bim
