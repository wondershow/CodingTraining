class Solution:
    """
    This problem is a dfs/bfs search problems. The key is the pruning strategy. 
    Otherwise it is a standard backtracking problem
    At the very begining, we compute how many chars (left, right) are supposed to be removed if we
    want to get a minimum removal to have it valid.
    
    Then during the DFS phase, we use a "quota" to guide use towards the final good resutls.
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def get_min_moves(s):
            left, right = 0, 0
            to_remove = [0, 0]
            for c in s:
                if c == "(":
                    left += 1
                elif c == ")":
                    right += 1
                if right > left:
                    to_remove[1] += 1
                    right -= 1
            to_remove[0] = left - right
            return to_remove
        
        def is_valid(path):
            left, right = 0, 0
            for c in path:
                if c == "(":
                    left += 1
                elif c == ")":
                    right += 1
                if left < right:
                    return False
            return left == right
        
        def dfs(s, index, path, res, del_left, del_right, left, right):
            if index == len(s) or right - left > del_right:
                if is_valid(path):
                    res.add("".join(path))
                return
            c = s[index]
            if c == "(" and del_left > 0:
                dfs(s, index + 1, path, res, del_left - 1, del_right, left, right)
            if c == ")" and del_right > 0:
                dfs(s, index + 1, path, res, del_left, del_right - 1, left, right)
            if c == "(":
                left += 1
            if c == ")":
                right += 1
            path.append(c)
            dfs(s, index + 1, path, res, del_left, del_right, left, right)
            path.pop()
            
        del_left, del_right = get_min_moves(s)
        res = set()
        dfs(s, 0, [], res, del_left, del_right, 0, 0)
        return list(res)
