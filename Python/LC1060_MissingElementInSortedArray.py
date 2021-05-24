class Solution:
    """
        We convert this problem to kth missing positive number.
        Some mistakes made:
        1. To covert this k to that k (the gap is nums[0] - 1 not nums[0])
        2. The hi is len(nums) not len(nums) - 1, since we want to cover the case when
        even the rightmost index is not the place we want. 
    """
    def missingElement(self, nums: List[int], k: int) -> int:
        k = (nums[0] - 1) + k
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] - (mid + 1) >= k:
                hi = mid
            else:
                lo = mid + 1
        #print(str(lo))
        return lo + k
