class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path, res = [], []
        def helper(res, path, pos):
            res.append(list(path))
            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                helper(res, path, i + 1)
                path.pop()
        helper(res, path, 0)
        return res
