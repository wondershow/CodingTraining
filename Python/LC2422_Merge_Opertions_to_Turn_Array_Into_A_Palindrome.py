class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums) - 1, 0
        while l < r:
            if nums[l] < nums[r]:
                nums[l + 1] += nums[l]
                l += 1
                res += 1
            elif nums[l] > nums[r]:
                nums[r - 1] += nums[r]
                r -= 1
                res += 1
            else:
                l, r = l + 1, r - 1
        return res
