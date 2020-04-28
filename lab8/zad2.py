from loadGraph import asNxGraph
import networkx as nx
import numpy as np
from numpy.linalg import matrix_power as mx_pow, norm

from zad1 import getNormAdjMatrix

def pageRankE(g: nx.DiGraph, e, d=0.85, eps=1e-8):
    """
    :return: page rank of given graph, implementation analogous to vertexRank2 method
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

gr = asNxGraph("graphs/some")
eps = 1e-4

print("\nsame value for each:")
d = 0.85
e = 1/len(gr)*np.ones(len(gr))
r = pageRankE(gr, e, d)
print(f"d={d}\n r={r}")
d = 0.5
r = pageRankE(gr, e, d)
print(f"d={d}\n r={r}")

print("\n[1 2 .. n] normalized by sum")
d = 0.85
e = np.array([i for i in range(1, len(gr)+1)])
e = e/sum(e)
r = pageRankE(gr, e)
print(f"d={d}\n r={r}")
d = 0.5
r = pageRankE(gr, e, d=0.5)
print(f"d={d}\n r={r}")

