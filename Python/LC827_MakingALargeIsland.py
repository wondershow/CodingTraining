class UF:
    def __init__(self, size):
        self.uf = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]
    
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.uf[rx] = ry
            self.sizes[ry] += self.sizes[rx]
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def component_size(self, x):
        return self.sizes[self.find(x)]
    
    def max_component(self):
        return max(self.sizes)

class Solution:
    """
        This solution uses a UF to keep track of connected components (islands).
        Then we iterate each "0" (water) blocks, try to "connect" all its 4 legit neibors's components to find a
        potential larger island by flipping a 0.
        
        Errors made:
        1. We need to add all 4 neighbors's (with dedupe by a set) size of a 0 cell, instead of only 2 neighbors.
        2. One edge case is when there is no water at all, that case we need to return the maximum component size
        Time O(n^2)
        Space O(n^2)
    """
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UF(n * n)
        deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for dx, dy in deltas:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                        uf.union(x * n + y, i * n + j)
        
        res = float("-inf")
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                area, components = 1, set()
                for dx, dy in deltas:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0  <= y < n and grid[x][y] == 1:
                        components.add(uf.find(x * n + y))
                for root in components:
                    area += uf.component_size(root)
                res = max(area, res)
                    
        return uf.max_component() if res == float("-inf") else res       
