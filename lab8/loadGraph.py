from typing import List, Tuple
import networkx as nx

def load_weighted_digraph(name: str) -> Tuple[int, List]:
    """Load a graph in the DIMACS ascii format (with weights) from
     the file "name" and return it as a list of sets
     Returns (V,L)
     V -- number of vertices (1, ..., V)
     L -- list of edges in the format (x,y,w): edge between x and y with weight w (x<y)"""

    V = 0
    L = []

    f = open(name, "r")
    lines = f.readlines()
    for l in lines:
        s = l.split()
        if len(s) < 1: continue
        if s[0] == "c":
            continue
        elif s[0] == "p":
            V = int(s[2])
        elif s[0] == "e":
            (a, b, c) = (int(s[1]), int(s[2]), int(s[3]))
            L.append((a, b, c))

    f.close()
    return V, L

def asNxGraph(name: str):
    V, L = load_weighted_digraph(name)
    G = nx.DiGraph()
    G.add_nodes_from([x for x in range(V)])
    for (u, v, weight) in L:  # ignore weight
        G.add_edge(u-1, v-1)
    return G