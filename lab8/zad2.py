import networkx as nx
import numpy as np
from numpy.linalg import matrix_power as mx_pow, norm

from zad1 import getNormAdjMatrix

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

    mu = np.random.rand(n)  # random state
    mu /= sum(mu)

    # finding stationary state (power method but normalization not necessary)
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)
    while norm(mu - mu@A) > eps:
        mu = mu @ mx_pow(A, 500)

    r = mu/norm(mu)  # normalizing result

    return r



