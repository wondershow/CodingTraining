class Solution:
  """
  The key of how to avoid duplicates when we enter the for loop, 
  check the curr val and its predecessor, make sure we do not skip same values.
  """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def helper(candidates, pos, remaining, path, res):
            if remaining <= 0:
                if remaining == 0:
                    res.append(list(path))
                return
            for i in range(pos, len(candidates)):

                # Here is the key
                if i != pos and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                helper(candidates, i + 1, remaining - candidates[i], path, res)
                path.pop()
        res = []
        helper(candidates, 0, target, [], res)
        return res
