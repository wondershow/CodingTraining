class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])
        seen = {(0, 0, k)}
        que = [(0, 0, k, 0)]
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while que:
            x, y, quota, steps = que.pop(0)
            if x == M - 1 and y == N - 1:
                return steps
            for dx, dy in deltas:
                x0, y0 = x + dx, y + dy
                if x0 < 0 or y0 < 0 or x0 >= M or y0 >= N:
                    continue
                if grid[x0][y0] == 0 and (x0, y0, quota) not in seen:
                    seen.add((x0, y0, quota))
                    que.append((x0, y0, quota, steps + 1))
                elif quota > 0 and (x0, y0, quota - 1) not in seen:
                    seen.add((x0, y0, quota - 1))
                    que.append((x0, y0, quota - 1, steps + 1))
        
        return -1
