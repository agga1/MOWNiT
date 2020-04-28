import numpy as np
from numpy.linalg import matrix_power as mx_pow, norm
import snap

""" Vertex rank analysis """


def getNormAdjMatrix(graph) -> np.array:
    """
    :param graph: labeled from 0
    :return:
     adjacency matrix n x n of @graph, where sum of each row = 1
     which makes A a transition matrix of markov chain
     (each row (state) describes probability of transition to other states (rows))
    """
    n = graph.GetNodes()
    A = np.zeros((n, n))
    for v in graph.Nodes():
        nv = v.GetOutDeg()
        for u in v.GetOutEdges():
            A[v.GetId(), u] = 1. / nv
    return A


def vertexRank(g, eps=1e-10, A=None):
    """
    :param g: graph with vertices labeled from 0, .. n-1
    :return: vertex rank
    """
    if A is None:
        A = getNormAdjMatrix(g)

    n = A.shape[0]
    mu = np.random.rand(n)
    mu /= sum(mu)  # random state

    # finding stationary state (power method but normalization not necessary, as A is a transition table)
    mu2 = mu @ A
    while norm(mu - mu2) > eps:
        mu = mu2
        mu2 = mu @ A

    return mu


def vertexRankFast(g, eps=1e-10, A=None):
    """ Stochastic interpretation of vertex rank - faster computation
    finding vertex rank using stationary state property of ergodic markov chains:
    1) mu is a stationary state <=> mu = mu*A
    2) stationary state mu = lim u*(A^n) (n->inf), where u- any state, A is a transition table
    :param g: graph with vertices labeled from 0, .. n-1
    :return: vertex rank
    """
    if A is None:
        A = getNormAdjMatrix(g)

    n = A.shape[0]
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)

    # finding stationary state (power method but normalization not necessary)
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)
    while norm(mu - mu @ A) > eps:
        mu = mu @ mx_pow(A, 100)

    return mu
