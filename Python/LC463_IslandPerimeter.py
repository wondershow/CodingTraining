class Solution:
    """
       For this problem, a natural way is doing a bfs or dfs. Although bfs /dfs might have same time complexity, the actual implmentation and runtime might be improved by following scanning soltuion.
       Just scan from left to right, top to bottom, when we see a 1, check its left and upper neigbhor. -2 if any land neighb found. 
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res
