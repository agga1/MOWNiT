from ex3dir.readGraph import *
import numpy as np
import networkx as nx
""" finds voltages on each node calculated using node analysis method """
def node_analysisNx(G: nx.Graph):
    A = np.zeros(shape=(len(G), len(G)))
    B = np.array([0]*len(G))
    ns = G.nodes
    for idx in ns:
        if ns[idx]['V'] is not None:
            A[idx][idx] = 1
            B[idx] = ns[idx]['V']
        else:
            for neigh in G[idx]:  # neigh = (v_idx, edge_weight)
                w = G[idx][neigh]['weight']
                A[idx][idx] += 1./w
                A[idx][neigh] -= 1./w
    Vs = np.linalg.solve(A, B)
    for idx in ns:
        ns[idx]['V'] = Vs[idx]
    return G


print("--!WARNING!-- current input type: first vertex with idx 0")
s, t, E = [int(x) for x in input("enter s, t and E values (separated by space)").split()]
Gnx = toNxGraph0("./graphs/cycle5")
Gnx.nodes[s]['V'] = E
Gnx.nodes[t]['V'] = 0

Gnx = node_analysisNx(Gnx)
print(*[Gnx.nodes[x] for x in Gnx.nodes])


