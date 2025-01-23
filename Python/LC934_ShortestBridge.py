class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            bfs_que.append([x, y, 0])
            grid[x][y] = -1
            for dx, dy in deltas:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] == 1:
                    dfs(x1, y1)

        M, N = len(grid), len(grid[0])
        deltas = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        bfs_que, visited, found = deque(), set(), False
        firstX, firstY = -1, -1
        for i in range(M):
                if found:
                    break
                for j in range(N):
                    if grid[i][j] == 1:
                        firstX, firstY = i, j
                        found = True
                        break

        dfs(firstX, firstY)
        
        res = 0
        while bfs_que:
            x, y, steps = bfs_que.popleft()
            for dx, dy in deltas:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < M and 0 <= y1 < N and grid[x1][y1] != -1:
                    if grid[x1][y1] == 1:
                        return steps
                    grid[x1][y1] =-1
                    bfs_que.append([x1, y1, steps + 1])
        return res
        

        
        
            
