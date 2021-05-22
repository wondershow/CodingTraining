class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= 0:
                hi = mid
            else:
                lo = mid + 1
        l, r = lo - 1, lo
        res = []
        while l >= 0 or r < len(nums):
            l_val = float("inf") if l < 0 else nums[l]
            r_val = float("inf") if r == len(nums) else nums[r]
            if abs(l_val) < abs(r_val):
                res.append(l_val * l_val)
                l -= 1
            else:
                res.append(r_val * r_val)
                r += 1
        return res
