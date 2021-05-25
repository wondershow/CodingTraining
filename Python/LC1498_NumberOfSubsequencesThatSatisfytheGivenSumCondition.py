class Solution:
    """
    For this problem 
    1. The order of numbers does not affect the final result, so we sort it first
    2. to find pairs that a + b <= target, it is like 2sum.
    l, r, whatever between l + 1 to r meets the requirement. we add 2**(r - l) to result
    
    Mistakes made:
    1. The while condition is lo <= hi, not lo < hi (this is not binary search)
    2. The i, j need to move in each while iteration (infinite loop)
    
    
    """
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        res, j, N = 0, 0, len(nums)
        lo, hi = 0, N - 1
        mod = 10 ** 9 + 7
        while lo <= hi:
            if nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                res = (res + pow(2, hi - lo, mod)) % mod
                lo += 1    
            
        
        return res
