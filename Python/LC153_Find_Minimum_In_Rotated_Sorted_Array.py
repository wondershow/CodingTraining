class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid
            else:
                hi = mid
        return min(nums[lo], nums[hi])
