class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, seen, running_sum = 0, {0 : 1}, 0
        for num in nums:
            running_sum += num
            res += seen.get(running_sum - k, 0)
            seen[running_sum] = seen.get(running_sum, 0) + 1
        return res
