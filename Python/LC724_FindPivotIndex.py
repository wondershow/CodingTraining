class Solution:
    
    """
    A better solution. 
    """
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - num - left_sum:
                return i
            left_sum += num
        return -1
    
    
    def pivotIndex1(self, nums: List[int]) -> int:
        N = len(nums)
        right = [0] * (N + 1)
        running_sum = 0
        for i in range(N - 1, -1, -1):
            running_sum += nums[i]
            right[i] = running_sum
            
        running_sum_left = 0
        for i in range(N):
            if running_sum_left == right[i + 1]:
                return i
            running_sum_left += nums[i]
        return -1
