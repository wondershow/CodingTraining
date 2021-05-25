class Solution:
    """
    Use the old template!!!
    """
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[lo]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid
                else:
                    hi = mid
        if nums[lo] == target:
            return lo
        if nums[hi] == target:
            return hi
        return -1
