class Set:
    def __init__(self, parent=None):
        self.rank = 0
        self.parent = self if parent is None else parent

    def find_parent(self):
        if self.parent != self:
            parent = self.parent.find_parent()
            self.parent = parent
            return parent
        return self


class DisjointUnionSets:
    def __init__(self, array=None):
        self.sets = {}
        if array is not None:
            self.fromarray(array)

    def fromarray(self, array):
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                if array[i, j] == 1:
                    self.sets[(i, j)] = Set()

    def union(self, key1, key2):
        par1 = self.sets[key1].find_parent()
        par2 = self.sets[key2].find_parent()
        if par1 == par2:
            return
        if par1.rank < par2.rank:
            par1.parent = par2
        elif par2.rank < par1.rank:
            par2.parent = par1
        else:
            par2.parent = par1
            par1.rank += 1


def find_disjoint(bin_array):
    """
    :return: leaders of disjoint sets of ones
    """
    # create and join all necessary sets
    sets = DisjointUnionSets(bin_array)
    xs, ys = bin_array.shape
    for i in range(xs):
        for j in range(ys):
            if bin_array[i, j] == 0:
                continue
            for currx in range(max(0, i - 1), min(xs, i + 2)):
                for curry in range(max(0, j - 1), min(ys, j + 2)):
                    if currx == i and curry == j:
                        continue
                    if bin_array[currx, curry] == 1:
                        sets.union((i, j), (currx, curry))
    # find all leaders
    leaders = []
    for key, mset in sets.sets.items():
        if mset.parent == mset:
            leaders.append(key)
    return leaders
