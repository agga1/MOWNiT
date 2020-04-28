from loadGraph import asNxGraph
import networkx as nx
import numpy as np
from numpy.linalg import matrix_power as mx_pow, norm

from time_eval import time_eval
from zad1 import getNormAdjMatrix


def pageRank(g: nx.DiGraph, d=0.85, eps=1e-8):
    """
    :return: page rank of given graph, implementation analogous to vertexRank2 method
    """
    A = getNormAdjMatrix(g)
    n = len(g)
    # add probability of random jump (and rescale A by d to maintain transition table property)
    A = d*A
    A += (1-d)/n

    n = len(g)
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)

    # finding stationary state (power method but normalization not necessary)
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)
    while norm(mu - mu@A) > eps:
        mu = mu @ mx_pow(A, 500)

    r = mu/norm(mu)  # normalizing result

    return r

gr = asNxGraph("graphs/some")
eps=1e-4
r1 = pageRank(gr)
print("page rank:", r1)
time_eval(pageRank, "page rank", 4, gr, eps)

