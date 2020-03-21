import networkx as nx
import numpy as np
from zad3.nodeAnalysis import normalize


def check(G: nx.DiGraph, shape=None)-> bool:
    I_sum =np.array([0.]*len(G.nodes()))
    for (u, v, attrs) in G.edges(data=True):
        u_norm = normalize(u, shape)
        v_norm = normalize(v, shape)
        I_sum[u_norm] -= attrs['current']
        I_sum[v_norm] += attrs['current']
    s, t = 0, 0
    eps = 1e-10
    for val in I_sum:
        if abs(val) > eps:
            if s==0:
                s = val
            elif t==0:
                t = val
            else:
                return False
    if abs(s+t) < eps:
        print(f"current in whole circuit: {abs(round(s, 9))}")
        return True
    return False