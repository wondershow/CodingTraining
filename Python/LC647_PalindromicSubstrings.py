class Solution:
    
    """
    Need to be careful about the boundary conditions
    when populating the dp
    """
    def countSubstrings1(self, s: str) -> int:
        N = len(s)
        dp = [[False] * N  for _ in range(N)]
        res = 0
        for i in range(N - 1):
            if s[i] == s[i + 1]:
                res += 1
                dp[i][i + 1] = True
            dp[i][i] = True
        dp[N - 1][N - 1] = True
        
        res += N
        for size in range(3, N + 1):
            for l in range(N - size + 1):
                r = l + size - 1
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    res += 1
        #print(dp)
        return res
    
    def countSubstrings(self, s: str) -> int:
        res = 0
        def count_helper(s, l, r):
            count = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                count += 1
                l, r = l - 1, r + 1
            return count
    
        for i in range(len(s)):
            res += count_helper(s, i, i)
            if i > 0:
                res += count_helper(s, i - 1, i)
        return res
