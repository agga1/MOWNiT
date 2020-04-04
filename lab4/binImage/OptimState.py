
class OptimState:
    def __init__(self, x0, cost):
        self.val = x0
        self.cost = cost

    def __repr__(self):
        print(self.val)
        print(self.cost)