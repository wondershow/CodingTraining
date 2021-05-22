class Solution:
    """
        Memoization.
        The key is cut string into two parts, left and right. 
        If right is in worddict, recursively call with left.
        
        Time complexity O(N^2) ( Not very clear. need to think more)
        
        Space complexity O(N*W)
        
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(string, memo, word_dict):
            if string in word_dict:
                return True
            if string in memo:
                return memo[string]
            for i in range(1, len(string)):
                if string[i:] in wordDict and helper(string[:i], memo, word_dict):
                    memo[string] = True
                    return True
            memo[string] = False
            return False
        memo = {}
        res = helper(s, memo, set(wordDict))
        #print(memo)
        return res
