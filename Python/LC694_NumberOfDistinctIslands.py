class Solution:
    """
    For each island, we use its topmost, leftmost point as origin, get all its members, then sort it, 
    convert it to a sting(make it hashable). Then add it to a set
    return the size of the set
    """
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distint_islands = set()
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 2
                    offset = (i, j)
                    bfs = [(i, j)]
                    island = []
                    while bfs:
                        x, y = bfs.pop(0)
                        island.append((x - offset[0], y - offset[1]))
                        for dx, dy in deltas:
                            x1, y1 = x + dx, y + dy
                            if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] == 1:
                                grid[x1][y1] = 2
                                bfs.append((x1, y1))
                    island.sort()
                    
                    distint_islands.add(" ".join([str(a) for a in island]))
        return len(distint_islands)
