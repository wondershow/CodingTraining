class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq, visited = deque(), set()
        deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        M, N = len(grid), len(grid[0])
        count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    dq.append([0, i, j])
                    visited.add((i, j))
                if grid[i][j] != 0:
                    count += 1
        if count == 0:
            return 0
        while dq:
            minutes, x, y = dq.popleft()
            count -= 1
            if count == 0:
                return minutes
            for dx, dy in deltas:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < M and 0 <= y1 < N and (x1, y1) not in visited and grid[x1][y1] == 1:
                    visited.add((x1, y1))
                    dq.append([minutes + 1, x1, y1])

        return -1
