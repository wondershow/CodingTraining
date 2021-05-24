class Solution:
    """
    Sliding window
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        res, zeros, j = 0, 0, 0
        for i in range(len(nums)):
            while j < len(nums):
                if zeros == k and nums[j] == 0:
                    break
                if nums[j] == 0:
                    zeros += 1
                j += 1
            res = max(res, j - i)
            if nums[i] == 0:
                zeros -= 1
        return res
