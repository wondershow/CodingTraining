class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
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
