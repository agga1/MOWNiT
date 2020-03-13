import numpy as np
from typing import List

class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()              # set of neighbours with edge weight
        self.V = None                 # voltage on this node

    def connect_to(self, v, weight):
        self.out.add((v, weight))

    def __repr__(self):
        return "nr "+str(self.idx)+" with voltage: "+str(self.V)

# without using networkx library
def create_nodes(V, L) -> List[Node]:
    G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, weight) in L:
        G[u].connect_to(v, weight)
        G[v].connect_to(u, weight)
    return G

def load_and_create_nodes(name: str):
    V, L = load_weighted_graph(name)
    return create_nodes(V, L)

def create_nodes_frst0(V, L) -> List[Node]:
    G = [Node(i) for i in range(0, V)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, weight) in L:
        G[u-1].connect_to(v-1, weight)
        G[v-1].connect_to(u-1, weight)
    return G

def load_and_create_nodes_frst0(name: str):
    V, L = load_weighted_graph(name)
    return create_nodes_frst0(V, L)


def node_analysis(G: List[Node]):
    A = np.zeros(shape=(len(G), len(G)))
    B = np.array([0]*len(G))
    for node in G:
        idx = node.idx
        if node.V is not None:
            A[idx][idx] = 1
            B[idx] = node.V
        else:
            for neigh in node.out:  # neigh = (v_idx, edge_weight)
                A[idx][idx] += 1./neigh[1]
                A[idx][neigh[0]] -= 1./neigh[1]
    Vs = np.linalg.solve(A, B)
    for node in G:
        node.V = Vs[node.idx]
