class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        que, seen = [], []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "*":
                    que = [(i, j, 0)]
                    seen = {(i, j)}
                    break
        
        deltas = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        while que:
            x, y, dist = que.pop(0)
            if grid[x][y] == '#':
                return dist
            for dx, dy in deltas:
                x0, y0 = x + dx, y + dy
                if 0 <= x0 < M and 0 <= y0 < N and (x0, y0) not in seen and grid[x0][y0] in ['#', 'O']:
                    seen.add((x0, y0))
                    que.append((x0, y0, dist + 1))
        return -1
