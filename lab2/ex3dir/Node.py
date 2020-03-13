
class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()              # set of neighbours with edge weight
        self.V = None                 # voltage on this node

    def connect_to(self, v, weight):
        self.out.add((v, weight))

    def __repr__(self):
        return "nr "+str(self.idx)+" with voltage: "+str(self.V)
