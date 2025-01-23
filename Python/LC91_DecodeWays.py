class Solution:
    def numDecodings1(self, s: str) -> int:
        memo, N = {-1:1}, len(s)
        for i in range(N):
            memo[i] = memo[i - 1]
            if s[i] == '0':
                if i > 0 and s[i - 1]  in ["1", "2"]:
                    memo[i] = memo[i - 2]
                    continue
                else:
                    return 0
            if i > 0 and 10 <= int(s[i-1:i+1]) <= 26:
                memo[i] += memo[i - 2]
        return memo[N - 1]

    def numDecodings2(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def helper(string, index):
            if index == len(string):
                return 1
            if string[index] == "0":
                return 0
            if index == len(string) - 1:
                return 1
            if 10 <= int(string[index : index + 2]) <= 26:
                return helper(string, index + 1) + helper(string, index + 2)
            else:
                return helper(string, index + 1)
        return helper(s, 0)

    def numDecodings(self, s: str) -> int:
        N = len(s)
        dp = [0] * (N + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(1, N):
            if s[i] != "0":
                dp[i + 1] = dp[i]
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]


        
