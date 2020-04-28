import networkx as nx
import numpy as np
from zad1 import getNormAdjMatrix, vertexRankFast


def pageRankE(g: nx.DiGraph, e, d=0.85, eps=1e-8):
    """
    :return: page rank of given graph, using fastest implementation from previous exercise
    """
    A = getNormAdjMatrix(g)

    # add probability of random jump (and rescale A by d to maintain transition table property)
    n = len(g)
    A = d*A
    R = np.tile((1-d)*e, (n, 1))
    A += R

    r = vertexRankFast(g, eps, A)

    return r



