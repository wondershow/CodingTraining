class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return nums[0]
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
