import networkx as nx
def get_random_connected(n: int, density=0.5):
    G = nx.erdos_renyi_graph(n, density)
    while not nx.is_connected(G):
        G = nx.erdos_renyi_graph(n, density)
    return G

def get_bridge_graph(n: int, density=0.5):
    A = get_random_connected(n, density)
    B = get_random_connected(n, density)
    rename = {}
    for idx in A.nodes():
        rename[idx] = idx+n
    B = nx.relabel_nodes(B, rename)
    C = nx.compose(A, B)
    C.add_edge(3, n+2)
    return C
