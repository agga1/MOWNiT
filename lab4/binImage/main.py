import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from SA import SAforBinImage
from energyFunctions import energyFuncStripes, energyFuncClassic
from generator import createBinImage
from nextState import nextStateRnd, nextStateNeigh
import os
names = ["Classic", "Stripes"]
name = names[1]

def runWithParams(n, d, energyFunc, nextStateFunc, subfolderName, neighNr, nameData=""):
    outDir = "results"
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    if not os.path.exists(f"{outDir}/{subfolderName}"):
        os.mkdir(f"{outDir}/{subfolderName}")
    bim = createBinImage(n, d)
    plt.imsave(f'{outDir}/{subfolderName}/input{neighNr}_{nameData}.png', bim, cmap=cm.gray)
    res = SAforBinImage(energyFunc, bim, nextStateFunc, neighNr=16, iter=15200, show=800)
    plt.imsave(f'{outDir}/{subfolderName}/result{neighNr}_{nameData}.png', res.val, cmap=cm.gray)

runWithParams(64, 0.2, energyFuncClassic, nextStateNeigh, "classic", 16, "n64")

