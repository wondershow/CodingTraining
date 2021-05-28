class Solution:
    """
    Backpack problem
    """
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(2)]
        dp[0][0], running_sum = True, 0
        for i, num in enumerate(nums):
            running_sum += num
            for j in range(1, min(target, running_sum) + 1):
                dp[(i + 1)%2][j] = dp[i % 2][j]
                if j >= num and dp[i % 2][j - num]:
                    dp[(i + 1) % 2][j] = True
        
        #for line in dp:
        #    print(line)
        
        return dp[len(nums) % 2][target]
