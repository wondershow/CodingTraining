class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        A typical binary search problem. We use one bin-search to address the problem.
        The findFirst finds 
        <, <, <, <, >=, >=, >=
        the index first >= of a target
        """
        def findFirst(val):
            lo, hi = 0, len(nums) - 1
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if nums[mid] < val:
                    lo = mid
                else:
                    hi = mid
            if nums[lo] >= val:
                return lo
            return hi

        # Edge case 1, the input is empty
        if not nums:
            return [-1, -1]

        lo = findFirst(target)
        hi = findFirst(target + 1)

        # Edge case 2, the target does not exist in the input
        if nums[lo] != target:
            return [-1, -1]
        
        # Edge case3, the "next big" element ends up as the last target position
        if nums[hi] == target:
            return [lo, hi]
        
        return [lo, hi - 1]
