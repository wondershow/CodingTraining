class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res, index):
            res.append(list(path))
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(nums, path, res, i + 1)
                path.pop()
        res = []
        dfs(nums, [], res, 0)
        return res
