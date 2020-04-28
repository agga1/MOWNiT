import snap

from time_eval import time_eval
from zad1 import vertexRank, vertexRankFast
from zad2 import pageRankE
import numpy as np

gr = snap.TNGraph.New()
for i in range(0, 5):
    gr.AddNode(i)
for i in range(0, 4):
    gr.AddEdge(i, i+1)
gr.AddEdge(4, 0)
gr.AddEdge(1, 3)
gr.AddEdge(0, 3)
n = gr.GetNodes()

""" task 1 summary """
eps = 1e-10

_, res =time_eval(vertexRank, "vertex rank", 10, gr, eps)
time_eval(vertexRankFast, "vertex rank using ergodic markov chain property", 10, gr, eps)

""" task 2 summary """

print("\ne = same value for each:")
eps = 1e-4
d = 0.85
e = 1/n*np.ones(n)
r = pageRankE(gr, e, d)
print(f"d={d}\n r={r}")
d = 0.5
r = pageRankE(gr, e, d)
print(f"d={d}\n r={r}")

print("\n e = [1 2 .. n] normalized by sum")
d = 0.85
e = np.array([i for i in range(1, n+1)])
e = e/sum(e)
r = pageRankE(gr, e)
print(f"d={d}\n r={r}")
d = 0.5
r = pageRankE(gr, e, d=0.5)
print(f"d={d}\n r={r}")