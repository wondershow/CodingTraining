class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        dp[i][j] means how many deleteions needed to make s[i:j + 1] a palinedrome
        dp[i][j] = min(1 + dp[i + 1][j], 1 + dp[i][j - 1])
                            
        """
        N = len(s)
        dp = [[float("inf")] * N for _ in range(N)]
        
        for i in range(N):
            dp[i][i] = 0
            
        for size in range(2, N + 1):
            for i in range(N - size + 1):
                j = i + size - 1
                dp[i][j] = min(dp[i][j], 1 + min(dp[i + 1][j], dp[i][j - 1]))
                if s[i] == s[j]:
                    if size == 2:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])
                
        
        return dp[0][N - 1] <= k
