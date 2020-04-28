from loadGraph import asNxGraph
from time_eval import time_eval
from zad1 import vertexRank, vertexRankFast
from zad2 import pageRankE
import numpy as np

""" task 1 summary """

gr = asNxGraph("graphs/some")
eps = 1e-10

time_eval(vertexRank, "vertex rank", 10, gr, eps)
time_eval(vertexRankFast, "vertex rank using ergodic markov chain property", 10, gr, eps)

""" task 2 summary """

gr = asNxGraph("graphs/some")
print("\ne = same value for each:")
eps = 1e-4
d = 0.85
e = 1/len(gr)*np.ones(len(gr))
r = pageRankE(gr, e, d)
print(f"d={d}\n r={r}")
d = 0.5
r = pageRankE(gr, e, d)
print(f"d={d}\n r={r}")

print("\n e = [1 2 .. n] normalized by sum")
d = 0.85
e = np.array([i for i in range(1, len(gr)+1)])
e = e/sum(e)
r = pageRankE(gr, e)
print(f"d={d}\n r={r}")
d = 0.5
r = pageRankE(gr, e, d=0.5)
print(f"d={d}\n r={r}")