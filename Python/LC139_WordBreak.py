class Solution(object):
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        This is a top down DP solutions.
        For each problem (substring), we break it into two parts left and right. We check if left is a seen problem and true, then solve the solve the problem on the right. 

        N - string length
        The time complexity is O(N^2).
        There are N states we need to put into memo, in each state we iterate the substring to find a word.
        """
        memo = {x : True for x in wordDict}
        def helper(string, memo):
            if string in memo:
                return memo[string]
            for i in range(1, len(string)):
                if memo.get(string[i:], False) and helper(string[:i], memo):
                    memo[string] = True
                    return True
            memo[string] = False
            return False
        res = helper(s, memo)
        return res

    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        This is a bottom up DP. The intial condition (dp[0]) is empty string which means in dictionary. We extend the substring from size 1 to N. At each iteration, break the substring with left, and right, the left is already cached, check the right parth is in the dictionary. If yes, that substring is "do-able".
        
        Time Complexity O(N^2) if substring is not considered
        """
        N = len(s)
        dp = [False] * (N + 1)
        dp[0], wordDict = True, set(wordDict)
        for i in range(1, N + 1):
            for j in range(i):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
