class Solution:
        """
        We do not need a visited set to remember path, since it is impossible to travel back to a node on the same path
        due to the fact that big values can go to smaller values, not vise versa. 
        """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        deltas = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        M, N = len(matrix), len(matrix[0])
        def dfs(matrix, x, y, memo):
            if (x, y) in memo:
                return memo[(x, y)]
            res = 1
            nonlocal deltas, M, N
            for dx, dy in deltas:
                i, j = dx + x, dy + y
                if i < 0 or j < 0 or i >= M or j >= N:
                    continue
                if matrix[i][j] < matrix[x][y]:
                    res = max(res, 1 + dfs(matrix, i, j, memo))
            memo[(x, y)] = res
            return res
        res, memo = 0, {}
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(matrix, i, j, memo))
        return res
