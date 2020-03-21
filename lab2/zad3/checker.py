import networkx as nx
def check(G: nx.DiGraph, s)-> bool:
    for idx in G.nodes():
        for (u, v, attrs) in G.edges(data=True):
            pass