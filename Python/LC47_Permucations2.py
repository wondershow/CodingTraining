class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used, res, path = set(), [], []
        nums.sort()

        def helper(used, res, path):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                # When an earlier duplicate is not used, we skip
                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in used:
                    continue
                if i in used:
                    continue
                used.add(i)
                path.append(nums[i])
                helper(used, res, path)
                path.pop()
                used.remove(i)
        helper(used, res, path)
        return res
