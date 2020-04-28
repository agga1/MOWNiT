from loadGraph import asNxGraph
import networkx as nx
import numpy as np
from numpy.linalg import matrix_power as mx_pow, norm
from time import perf_counter


def getAdjMatrix(graph: nx.DiGraph)-> np.array:
    """
    :param graph: labeled from 0
    :return: np.array n x n
    """
    n = len(graph)
    A = np.zeros((n, n))
    for v in graph:
        for u in graph[v].keys():
            # print("edge", v, u)
            A[v, u] = 1./n
    return A

def vertexRank(g: nx.DiGraph, eps=1e-10):
    """ simple vertex rank implementation
    :param g: graph with vertices labeled from 0, .. n-1
    :return: vertex rank
    """
    A = getAdjMatrix(g)
    d = np.sum(A, axis=1).reshape(-1, 1)
    A /= d

    # power method implementation
    st1 = perf_counter()
    n = len(g)
    r = np.random.rand(n)
    r /= norm(r)
    r2 = r @ A
    while(norm(r2-r) > eps):
        r = r2/norm(r2)
        r2 = r@A
    st2 = perf_counter()
    print(st2-st1)
    return r

def vertexRank2(g: nx.DiGraph, eps=1e-10):
    """ Stochastic interpretation of vertex rank
    finding vertex rank using stationary state property of ergodic markov chains:
    1) mu is a stationary state <=> mu = mu*A
    2) stationary state mu = lim u*(A^n) (n->inf), where u- any state, A is a transition table
    :param g: graph with vertices labeled from 0, .. n-1
    :return: vertex rank
    """
    A = getAdjMatrix(g)
    d = np.sum(A, axis=1).reshape(-1, 1)
    # I normalize each row so that sum(row) = 1,
    #  which makes A a transition matrix of markov chain
    # (each row (state) describes probability of transition to other states (rows))
    A /= d
    n = len(g)
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)

    # finding stationary state (power method but normalization not necessary)
    st1 = perf_counter()
    mu2 = mu@A
    while norm(mu-mu2) > eps:
        mu = mu2
        mu2 = mu@A

    st2 = perf_counter()
    print(st2-st1)
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
    A = getAdjMatrix(g)
    d = np.sum(A, axis=1).reshape(-1, 1)
    # I normalize each row so that sum(row) = 1,
    #  which makes A a transition matrix of markov chain
    # (each row (state) describes probability of transition to other states (rows))
    A /= d
    n = len(g)
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)

    # finding stationary state (power method but normalization not necessary)
    st1 = perf_counter()
    mu = np.random.rand(n)  # random state
    mu /= sum(mu)
    while norm(mu - mu@A) > eps:
        mu = mu @ mx_pow(A, 500)

    st2 = perf_counter()
    print(st2-st1)
    r = mu/norm(mu)  # normalizing result
    return r

gr = asNxGraph("graphs/some")
eps = 1e-10
r1 = vertexRank(gr, eps)
r2 = vertexRank2(gr, eps)
r3 = vertexRank3(gr, eps)


