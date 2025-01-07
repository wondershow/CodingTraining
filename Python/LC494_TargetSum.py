class Solution:
    """
    Intersting when the input size is 24, 2^24 will not work anymore.
    So we have to use memo.
    """
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(nums, index, remain, memo):
            if index == len(nums):
                if remain == 0:
                    return 1
                return 0
            if (index, remain) in memo:
                return memo[(index, remain)]
            res = 0
            res += dfs(nums, index + 1, remain - nums[index], memo)
            res += dfs(nums, index + 1, remain + nums[index], memo)
            memo[(index, remain)] = res
            return res
            
        
        return dfs(nums, 0, target, {})
