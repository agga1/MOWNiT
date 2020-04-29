import numpy as np
from zad1 import getNormAdjMatrix, vertexRankFast, vertexRank


def pageRankE(g, e, d=0.85, eps=1e-8, max_iter=100, n=None):
    """
    :return: page rank of given graph, using implementation from previous exercise
    """
    A = getNormAdjMatrix(g, n)

    # add probability of random jump (and rescale A by d to maintain transition table property)
    n = A.shape[0] if n is None else n
    A = d*A
    R = np.tile((1-d)*e, (n, 1))
    A += R

    r = vertexRank(g, eps, max_iter=max_iter, A=A)
    return r



