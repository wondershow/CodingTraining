class Solution:
    """
    This is a backtracking/permutation problem. This is the key. It is not a pure 
    recursion problem
    """
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(res, lremain, remain, path, n):
            if lremain == remain == n:
                res.append(path)
                return
            # remain >= lremain
            if remain < lremain:
                dfs(res, lremain, remain + 1, path + ")", n)
            if lremain < n:
                dfs(res, lremain + 1, remain, path + "(", n)
        
        res = []
        dfs(res, 0, 0, "", n)
        return res
