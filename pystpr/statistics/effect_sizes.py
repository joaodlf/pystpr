import math


class CohenD():
    def __init__(self, group1, group2):
        self._group1 = group1
        self._group2 = group2

    def compute(self):
        diff = self._group1.mean() - self._group2.mean()
        var1 = self._group1.var()
        var2 = self._group2.var()
        n1, n2 = len(self._group1), len(self._group2)
        pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
        return diff / math.sqrt(pooled_var)