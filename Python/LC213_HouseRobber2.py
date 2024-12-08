class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            N = len(arr)
            if N < 2:
                return arr[0]
            dp = [0] * N
            dp[0], dp[1] = arr[0], max(arr[0], arr[1])
            for i in range(2, N):
                dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
            return dp[-1]
        if len(nums) < 4:
            return max(nums)
        return max(helper(nums[1:]), helper(nums[:-1]))
