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

def isMatch2(self, s: str, p: str) -> bool:
        """
        From Tushar Roy. Not very clear but seems to be simpler
        State transtition:
        1. s[i] == p[j] or p[j] == '.':
            remove the current comparing chars and see if the prefix substrings match
        2. when p[j] == '*':
            2.1 when '*' means cancel, then match s[0...i] with p[0...j - 2]

            2.2 when '*' means not cancel but repeat AND s[i] == p[j - 1]
                then remove the last char in s[0..i] (we get s[0..i-1]) and match s[0...i-1] with p[0...j]
                The "removing" action means remove the repeat
        
        """
        M, N = len(s), len(p)
        dp = [[False] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = True
        for i in range(1, N, 2):
            if p[i] == '*':
                dp[0][i + 1] = True
            else:
                break 
        for i in range(M):
            for j in range(N):
                if s[i] == p[j] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                    continue
                if p[j] != '*':
                    continue

                # First case, match 'a' and 'ab*', let '*' cancel the previous character
                case1 = dp[i + 1][j - 1]

                # second case 'ba' vs 'ba*', in this case we remove the trailing letter
                # (we get 'b') and we match it with 'ba*'
                if p[j - 1] == "." or s[i] == p[j - 1]:
                    case1 = case1 or dp[i][j + 1]
                dp[i + 1][j + 1] = case1
        return dp[-1][-1]


    
    
