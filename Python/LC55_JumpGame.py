class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for index, steps in enumerate(nums):
            if max_reach < index:
                return False
            max_reach = max(max_reach, index + steps)
        return True
