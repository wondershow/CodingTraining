class Solution:
    """
    Not sure why the DFS version is not working
    Note that we can not use |i - x0| + |j - y0| to compute distance. 
    We have do use bfs 'd + 1', no idea why
    """
    def shortestDistance(self, grid: List[List[int]]) -> int:
        deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        M, N = len(grid), len(grid[0])
        count = [[0] * N for _ in range(M)]
        total_buildings = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    total_buildings += 1
                    que = [(i, j, 0)]
                    seen = {(i, j)}
                    while que: 
                        x, y, d = que.pop(0)
                        for dx, dy in deltas:
                            x1, y1 = x + dx, y + dy
                            if x1 < 0 or y1 < 0 or x1 == M or y1 == N:
                                continue
                            if grid[x1][y1] > 0 or (x1, y1) in seen:
                                continue
                            seen.add((x1, y1))
                            count[x1][y1] += 1
                            grid[x1][y1] -= d + 1
                            que.append((x1, y1, d + 1))
        res = float("inf")
        for i in range(M):
            for j in range(N):
                if grid[i][j] <= 0:
                    if count[i][j] == total_buildings:
                        res = min(res, -grid[i][j])
        #for line in grid:
        #    print(" ".join(['{0:05}'.format(a) for a in line]))
        return -1 if res == float("inf") else res
