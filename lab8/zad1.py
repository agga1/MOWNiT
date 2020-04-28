from loadGraph import asNxGraph
import networkx as nx
import numpy as np
from numpy.linalg import matrix_power as mx_pow, norm
from time_eval import time_eval


def getNormAdjMatrix(graph: nx.DiGraph)-> np.array:
    """
    :param graph: labeled from 0
    :return:
     adjacency matrix n x n of @graph, where sum of each row = 1
     which makes A a transition matrix of markov chain
     (each row (state) describes probability of transition to other states (rows))
    """
    n = len(graph)
    A = np.zeros((n, n))
    for v in graph:
        nv = len(graph[v])
        for u in graph[v].keys():
            A[v, u] = 1./nv
    return A


def vertexRank(g: nx.DiGraph, eps=1e-10):
    """ simple vertex rank implementation
    :param g: graph with vertices labeled from 0, .. n-1
    :return: vertex rank
    """
    A = getNormAdjMatrix(g)

    # power method implementation
    n = len(g)
    r = np.random.rand(n)
    r /= norm(r)
    r2 = r @ A
    while(norm(r2-r) > eps):
        r = r2/norm(r2)
        r2 = r@A

    return r

def vertexRank2(g: nx.DiGraph, eps=1e-10):
    """ Stochastic interpretation of vertex rank
    finding vertex rank using stationary state property of ergodic markov chains:
    1) mu is a stationary state <=> mu = mu*A
    2) stationary state mu = lim u*(A^n) (n->inf), where u- any state, A is a transition table
    :param g: graph with vertices labeled from 0, .. n-1
    :return: vertex rank
    """
    A = getNormAdjMatrix(g)

    n = len(g)
    mu = np.random.rand(n)
    mu /= sum(mu)   # random state

    # finding stationary state (power method but normalization not necessary)
    mu2 = mu@A
    while norm(mu-mu2) > eps:
        mu = mu2
        mu2 = mu@A

    r = mu/norm(mu)  # normalizing result
    return r

def vertexRank3(g: nx.DiGraph, eps=1e-10):
    """ Stochastic interpretation of vertex rank
    finding vertex rank using stationary state property of ergodic markov chains:
    1) mu is a stationary state <=> mu = mu*A
    2) stationary state mu = lim u*(A^n) (n->inf), where u- any state, A is a transition table
    :param g: graph with vertices labeled from 0, .. n-1
    :return: vertex rank
    """
    A = getNormAdjMatrix(g)

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
eps = 1e-5

time_eval(vertexRank, "standard power method", 4, gr, eps)
time_eval(vertexRank, "using stationary state def", 4, gr, eps)
time_eval(vertexRank, "using ergodic markov chain property", 4, gr, eps)


