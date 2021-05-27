class Solution:
    """
    Overall roadmap:
    1. Massage the nums array to set all non-positive number to a very large number like N + 2
    2. Scan the array, at index i, if its abs value can be mapped to an index between 0 and N - 1, flip
    the value at index to be negative
    3. First positive index + 1
    
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 2
        
        for i in range(len(nums)):
            
            index = abs(nums[i]) - 1
            # First mistake failed to check the left boundary of nums[i] - 1
            if index < len(nums):
                nums[index] = -abs(nums[index])
        
        #print(" ".join([str(a) for a in nums]))
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
