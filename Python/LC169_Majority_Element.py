class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, None
        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        return res
