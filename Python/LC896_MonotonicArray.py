class Solution:
    def isMonotonic1(self, nums: List[int]) -> bool:
        
        N, i = len(nums), 0
        while i < N - 1 and nums[i] <= nums[i + 1]:
            i += 1
        if i == N - 1:
            return True
        i = 0
        while i < N - 1 and nums[i] >= nums[i + 1]:
            i += 1
        if i == N - 1:
            return True
        return False
    
    """
    Index is devil!
    """
    def isMonotonic(self, nums: List[int]) -> bool:
        
        N, i, stored = len(nums), 0, 0
        for i in range(N - 1):
            if nums[i] - nums[i + 1] != 0:
                if (nums[i] - nums[i + 1]) * stored < 0:
                    return False
                stored = nums[i] - nums[i + 1]
        return True
