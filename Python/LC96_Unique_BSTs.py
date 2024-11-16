class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            res = 0
            for lsize in range(i):
                res += dp[lsize] * dp[i - lsize - 1]
            dp[i] = res
        return dp[-1]
