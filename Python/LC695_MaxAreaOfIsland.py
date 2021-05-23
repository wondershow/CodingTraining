class Solution:
    """
    Mistakes made:
    1 'grid[i][j] = 2' is needed before bfs starts
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res, M, N = 0, len(grid), len(grid[0])
        deltas = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    que = [(i, j)]
                    size = 0
                    while que:
                        x, y = que.pop(0)
                        size += 1
                        for dx, dy in deltas:
                            x1, y1 = x + dx, y + dy
                            if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] == 1:
                                grid[x1][y1] = 2
                                que.append((x1, y1))
                    res = max(res, size)
        return res
