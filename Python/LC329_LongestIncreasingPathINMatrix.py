"""
use an aux matrix memo to store the ans at each location.

at each locaiton ans = 1 + max(smaller neighbor's ans), memo will be used to 
remove redundcant computation 
"""
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        M, N = len(matrix), len(matrix[0])
        memo = [[-1] * N for j in range (M)]
        deltas = [0, 1], [1, 0], [0, -1], [-1, 0]

        # At (x, y), what is its longest path
        def dfs(x, y):
            if memo[x][y] != -1:
                return memo[x][y]
            res = 1
            for dx, dy in deltas:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < M and 0 <= y1 < N and matrix[x1][y1] > matrix[x][y]:
                    res = max(res, 1 + dfs(x1, y1))
            memo[x][y] = res
            return res
        
        res = 0
        for i in range(M):
            for j in range(N):
                if memo[i][j] == -1:
                    res = max(res, dfs(i, j))
        return res
