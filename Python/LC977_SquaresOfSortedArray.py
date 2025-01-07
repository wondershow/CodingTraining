class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res, i = [0] * len(nums), len(nums) - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[i] = abs(nums[r]) * abs(nums[r])
                i, r = i - 1, r - 1
            else:
                res[i] = abs(nums[l]) * abs(nums[l])
                i, l = i - 1, l + 1
        return res
