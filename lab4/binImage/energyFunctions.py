import numpy as np

def energyFuncStripes(bim, x, y, xOffs, yOffs, dist=None):
    n = bim.shape[0]
    if dist is None:
        dist = np.sqrt(xOffs**2+yOffs**2)
    if x+xOffs>=n or x+xOffs<0 or y+yOffs>=n or y+yOffs<0:
        return 0
    if bim[x, y]==bim[x+xOffs, y+yOffs]==1:
        return dist
    else:
        return 0


def energyFuncClassic(bim, x, y, xOffs, yOffs, dist=None):
    n = bim.shape[0]
    if dist is None:
        dist = np.sqrt(xOffs**2+yOffs**2)
    if x+xOffs>=n or x+xOffs<0 or y+yOffs>=n or y+yOffs<0:
        return 0
    if bim[x, y]==bim[x+xOffs, y+yOffs]==1:
        return 1/dist
    else:
        return 0



