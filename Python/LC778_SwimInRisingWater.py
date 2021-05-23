class Solution:
    """
    The heap method, 
    Mistakes made:
    fail to use the cost as the heap key
    """
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while heap:
            cost, x, y = heappop(heap)
            if x == y == N - 1:
                return cost
            for dx, dy in deltas:
                i, j = x + dx, y + dy
                if i < 0 or j < 0 or i >= N or j >= N:
                    continue
                if (i, j) in seen:
                    continue
                seen.add((i, j))
                heappush(heap, (max(cost, grid[i][j]), i, j))
        return -1
            
        
        
        
    """
    The Binary searh solution
    o(log(max - min) * N*N)
    """
    def swimInWater1(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def can_swim(grid, h):
            nonlocal M, N, deltas
            if grid[0][0] > h or grid[M - 1][N - 1] > h:
                return False
            que, seen = [(0, 0)], {(0, 0)}
            while que:
                x, y = que.pop(0)
                if x == M - 1 and y == N - 1:
                    return True
                for dx, dy in deltas:
                    i, j = x + dx, y + dy
                    if i < 0 or j < 0 or i >= M or j >= N:
                        continue
                    if (i, j) in seen or grid[i][j] > h:
                        continue
                    que.append((i, j))
                    seen.add((i, j))
            return False
        
        lo, hi = 0, M * M
        
        while lo < hi:
            mid = (lo + hi) // 2
            if can_swim(grid, mid):
                hi = mid 
            else:
                lo = mid + 1
                
        return lo
