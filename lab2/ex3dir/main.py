from ex3dir.nodeAnalysis import *
from ex3dir.readGraph import *

# Gnx = toNxGraph0("./graphs/cycle5")
# Gnx = nx.grid_2d_graph(5, 6)
Gnx = nx.fast_gnp_random_graph(20, 0.2)
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
