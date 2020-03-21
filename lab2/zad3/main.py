from zad3.nodeAnalysis import *
from zad3.readGraph import *

# Gnx = toNxGraph0("./graphs/simple5")
# Gnx = nx.grid_2d_graph(5, 6)
Gnx = nx.fast_gnp_random_graph(10, 0.2)
add_attr(Gnx)
# for idx, val in list(Gnx.nodes()):
#     print(idx, val)
# print(Gnx.nodes())
print("--!WARNING!-- current input type: first vertex with idx 0")
s, t, E = [int(x) for x in input("enter s, t and E values (separated by space)").split()]
Gnx.nodes[t]['V'] = 0
Gnx.nodes[s]['V'] = E

node_analysisNx(Gnx)
# print(*[Gnx.nodes[x] for x in Gnx.nodes])
update_current(Gnx)
print(list(Gnx.edges(data=True)))

"""
3.wystarczy albo kirch albo wezly
brakuje m-n+1 cyklow prostych networkx do cyklow
networkx -> get random graph
jet color map (prąd wysoki - czerwony niski -nieb
napisz skrypt sprawdzający sume napiec (czy 0)- czy poprawny alg
uklady rownan nadokreslone
"""
