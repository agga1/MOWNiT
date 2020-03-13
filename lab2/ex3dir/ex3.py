from ex3dir.readGraph import *
import numpy as np

G = load_and_create_nodes("./graphs/cycle5")
print("--!WARNING!-- vertices nr from 1..n")
s, t, E = [int(x) for x in input("enter s, t and E values (separated by space)").split()]
# print(s+2)
G[s].V = E
G[t].V = 0
print([G[x] for x in range(1, len(G))])

"""
create matrix VxV , V- nr of nodes in graph
"""
def node_analysis(G: List[Node])-> List[List[float]]:

    for node in G:
        if(node.V is not None):
            continue

