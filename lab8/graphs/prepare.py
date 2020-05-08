from random import randint
import snap

""" making sure each row is a non-zero vector"""
G = snap.LoadEdgeList(snap.PNGraph, "stanford4000.txt", 0, 1)
n = 4000
for i in range(n):
    if not G.IsNode(i):
        G.AddNode(i)
for v in G.Nodes():
    if v.GetOutDeg() == 0:
        x = randint(0, n - 1)
        x = x if x != v.GetId() else (x+1)%n
        G.AddEdge(v.GetId(), randint(0, n-1))

snap.SaveEdgeList(G, "stanford4000ok.txt", "tab-separated list of edges")
