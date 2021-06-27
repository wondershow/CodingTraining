class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x, y, x0, y0, grid, c, seen):
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            M, N = len(grid), len(grid[0])
            res = False
            for dx, dy in directions:
                a, b = x + dx, y + dy
                if a < 0 or a == M or b < 0 or b == N:
                    continue
                if a == x0 and b == y0:
                    continue
                if grid[a][b] != c:
                    continue
                if (a, b) in seen:
                    return True
                seen.add((a, b))
                res |= dfs(a, b, x, y, grid, c, seen)
            return res
            
            
        
        M, N = len(grid), len(grid[0])
        seen = set()
        for i in range(M):
            for j in range(N):
                if (i, j) not in seen:
                    seen.add((i, j))
                    if dfs(i, j, -1, -1, grid, grid[i][j], seen):
                        return True
        return False
                    
