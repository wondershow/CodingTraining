   class Solution:
    """
        This problem is tricky. The key is we need to look up same (running sum % k) which is one index apart.
        To achieve that, we delay adding running sum to hash by one.
        Edge cases:
        1. When k = 1
        2. When there are 2 consecutive 0s
    """
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if k == 1:
            return True
        
        seen, running, pre = set(), 0, 0
        
        for i, v in enumerate(nums):
            running = (v + running) % k
            if i > 0 and v == 0 and nums[i - 1] == 0:
                return True
            if running in seen:
                return True
            seen.add(pre)
            pre = running
            #print("{} {} {} {}".format(seen, i, running, v))
        return False
            
