from ex3dir.nodeAnalysis import node_analysisNx
from ex3dir.readGraph import *

Gnx = toNxGraph0("./graphs/cycle5")
print("--!WARNING!-- current input type: first vertex with idx 0")
s, t, E = [int(x) for x in input("enter s, t and E values (separated by space)").split()]
Gnx.nodes[t]['V'] = 0
Gnx.nodes[s]['V'] = E

Gnx = node_analysisNx(Gnx)
print(*[Gnx.nodes[x] for x in Gnx.nodes])


