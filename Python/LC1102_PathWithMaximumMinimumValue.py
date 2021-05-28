class Solution:
    def maximumMinimumPath1(self, grid: List[List[int]]) -> int:
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def canTravel(grid, cost):
            nonlocal deltas
            R, C = len(grid), len(grid[0])
            if grid[0][0] < cost or grid[R - 1][C - 1] < cost:
                return False
            bfs = [(0, 0)]
            while bfs:
                x, y = bfs.pop(0)
                if x == R - 1 and y == C - 1:
                    return True
                for dx, dy in deltas:
                    x0, y0 = x + dx, y + dy
                    if 0 <= x0 < R and 0 <= y0 < C and grid[x0][y0] >= cost:
                        bfs.append((x0, y0))
            return False
        
        R, C = len(grid), len(grid[0])
        
        lo, hi = 0, 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if canTravel(grid, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    """Dijkstra"""
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        heap = [[-grid[0][0], 0, 0]]
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        M, N = len(grid), len(grid[0])
        seen = {(0, 0)}
        while heap:
            cost, x, y = heappop(heap)
            if x == M - 1 and y == N - 1:
                return -cost
            for dx, dy in deltas:
                i, j = x + dx, y + dy
                if 0 <= i < M and 0 <= j < N and (i, j) not in seen:
                    seen.add((i, j))
                    heappush(heap, [-min(-cost, grid[i][j]), i, j])
        
        return -1
