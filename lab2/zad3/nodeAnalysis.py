import numpy as np
import networkx as nx

def normalize(idx, shape=None):
    if (shape is None or len(shape) == 1):
        return idx
    if len(shape) == 2:
        return idx[0] * shape[1] + idx[1]


""" finds voltages on each node calculated using node analysis method 
@shape: index labels dimensions( ex (5,6) for 2d graph, (30)(or None) for classic ) """
def node_analysisNx(G: nx.Graph, shape=None):
    A = np.zeros(shape=(len(G), len(G)))
    B = np.array([0]*len(G))
    ns = G.nodes
    for idx in ns:
        idx_norm = normalize(idx, shape)  # if dx is not a single nr (e.g. 2dgrid->(0,1))
        if ns[idx]['V'] is not None:
            A[idx_norm][idx_norm] = 1
            B[idx_norm] = ns[idx]['V']
        else:
            for neigh in G[idx]:  # neigh = (v_idx, edge_weight)
                w = G[idx][neigh]['weight']
                A[idx_norm][idx_norm] += 1./w
                A[idx_norm][normalize(neigh, shape)] -= 1./w
    Vs = np.linalg.solve(A, B)
    for idx in ns:
        ns[idx]['V'] = Vs[normalize(idx, shape)]

def update_current(G: nx.Graph):
    for (u, v, props) in G.edges(data=True):
        props['current'] = abs(G.nodes[u]['V']-G.nodes[v]['V'])/props['weight']
