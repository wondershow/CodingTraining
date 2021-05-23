class Solution:
    """
        Mistakes made:
        1. Failed to init dp[0][0]
        2. When do a* extenstion a* => aa*, it is same as deleting one from s, so 
          for that case dp[i][j] = dp[i - 1][j] (this is the key)
    """
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if len(s) > 0 and len(p) == 0:
            return False
        M, N = len(s), len(p)
        """
        dp[i][j] means if s[:i + 1] matches p[:j + 1]
        
        if s[i] == p[j] or p[j] == ".":
            dp[i + 1][j + 1] = dp[i][j]
        elif p[j] == "*"
            if p[j - 1] != s[i] and p[j - 1] != "."
                dp[i + 1][j + 1] = dp[i + 1][j - 1]
            else: 
                dp[i + 1][j + 1] |= dp[i + 1][j] (* means last extenstion of its previous record)
                dp[i + 1][j + 1] |= dp[i][j + 1] (* means extenstion of previosu record)
                dp[i + 1][j + 1] != dp[i + 1][j - 1] (* means deletion)
            
        init 
        dp[0][i] = True if i % 2 == '*'
        
        ans dp[M][N]
        """
        
        dp = [[False] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = True
        i = 1
        while i < N and p[i] == '*':
            dp[0][i + 1] = True
            i += 2
        
        for i in range(M):
            for j in range(N):
                if s[i] == p[j] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == "*":
                    if p[j - 1] != s[i] and p[j - 1] != ".":
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] # * means cancellation
                    else:
                        #dp[i + 1][j + 1] |= dp[i][j - 1] # * means last extenstion of its previous record (a* = a)
                        #dp[i + 1][j + 1] |= dp[i][j + 1] # * means extension of previous char (a* means a*)
                        #dp[i + 1][j + 1] |= dp[i + 1][j - 1] #(* means deletion a* = "")
                        dp[i + 1][j + 1] = dp[i + 1][j - 1] or dp[i][j - 1] or dp[i][j + 1]
        #for line in dp:
         #   print(line)            
        return dp[M][N]
    
    
