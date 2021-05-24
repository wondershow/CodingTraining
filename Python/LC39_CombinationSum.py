class Solution:
    """
    
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, index, path, res, remains):
            if remains <= 0:
                if remains == 0:
                    res.append(list(path))
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(candidates, i, path, res, remains - candidates[i])                
                path.pop()
                
        res = []
        dfs(candidates, 0, [], res, target)
        return res
