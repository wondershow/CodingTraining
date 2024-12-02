class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        max_side = 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    max_side = 1
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == matrix[i - 1][j - 1] == matrix[i][j - 1] == matrix[i - 1][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
                else:
                    dp[i][j] = int(matrix[i][j])
                max_side = max(max_side, dp[i][j])
        return max_side * max_side
