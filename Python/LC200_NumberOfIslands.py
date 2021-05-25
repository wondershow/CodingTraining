class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res, M, N = 0, len(grid), len(grid[0])
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    res += 1
                    bfs = [(i, j)]
                    grid[i][j] = "2"
                    while bfs:
                        x, y = bfs.pop(0)
                        for dx, dy in deltas:
                            x0, y0 = x + dx, y + dy
                            if 0 <= x0 < M and 0 <= y0 < N and grid[x0][y0] == "1":
                                grid[x0][y0] = "2"
                                bfs.append((x0, y0))
        return res
        
