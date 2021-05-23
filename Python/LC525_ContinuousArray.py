class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen, running, res = {0: -1}, 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                running += 1
            else:
                running -= 1
            if running in seen:
                res = max(res, i - seen[running])
            else:
                seen[running] = i
        return res
