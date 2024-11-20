class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(2)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(n):
                if j > 0:
                    dp[i % 2][j] = dp[(i - 1)%2][j] + dp[i%2][j - 1]
                else:
                    dp[i % 2][j] = dp[(i - 1)%2][j]
        return dp[(m - 1)% 2][n - 1]
