class UnionFind:
    # use 0-index, safer!
    def __init__(self, cells):
        self.islands, self.uf = 0, [i for i in range(cells)]

    # i is 0 - based
    def _root(self, i):
        if self.uf[i] == i:
            return i
        print(f'i = {i}, self.uf[i] = {self.uf[i]}')
        self.uf[i] = self._root(self.uf[i])
        return self.uf[i]

    # i, j are 0-based
    def union(self, i, j):
        r1 = self._root(i)
        r2 = self._root(j)
        self.uf[r1] = r2
        if r1 != r2:
            self.islands -= 1

    def getIslands(self):
        return self.islands

    def addIsland(self):
        self.islands += 1


# This is a UionFind (UF) problem:
# Edge cases missed:
# 1. When the input is repeated
# 2. Need to use 0 based UF array
# 3. When to decrease island? When the root1 and root2 are different!
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf, lands = UnionFind(m * n), set()
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res, seen = [], set()
        for x, y in positions:
            if (x, y) not in seen:
                uf.addIsland()
                for dx, dy in deltas:
                    x1, y1 = x + dx, y + dy
                    if x1 < 0 or y1 < 0 or x1 == m or y1 == n or (x1, y1) not in lands:
                        continue
                    uf.union(x * n + y, x1 * n + y1)
                lands.add((x, y))
            seen.add((x, y))
            res.append(uf.getIslands())
        return res
