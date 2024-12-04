class UnionFind:
    def __init__(self, size):
        self.uf = [i for i in range(size)]
        self.size = [1 for i in range(size)]
    
    def find(self, x):
        if self.uf[x] != x:
            return self.find(self.uf[x])
        return self.uf[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.uf[rx] = ry
            self.size[ry] += self.size[rx]

    def isLandSize(self, x):
        root = self.find(x)
        return self.size[root]

    def maxIslandSize(self):
        return max(self.size)

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        uf = UnionFind(M * N)
        for i in range(M):
            for j in range(N):
                if i > 0 and grid[i][j] == grid[i - 1][j] == 1:
                    uf.union(i * N + j, (i - 1) * N + j)
                if j > 0 and grid[i][j] == grid[i][j - 1] == 1:
                    uf.union(i * N + j, i * N + j - 1)
        
        maxIslandSize = uf.maxIslandSize()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    roots = set()
                    if i > 0 and grid[i - 1][j] == 1:
                        roots.add(uf.find((i - 1) * N + j))
                    if j > 0 and grid[i][j - 1] == 1:
                        roots.add(uf.find(i * N + j - 1))
                    if i < M - 1 and grid[i + 1][j] == 1:
                        roots.add(uf.find((i + 1) * N + j))
                    if j < N - 1 and grid[i][j + 1] == 1:
                        roots.add(uf.find(i * N + j + 1))
                    size = 1
                    for root in roots:
                        size += uf.isLandSize(root)
                    maxIslandSize = max(maxIslandSize, size)
        return maxIslandSize

