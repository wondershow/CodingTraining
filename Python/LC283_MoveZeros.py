class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.


        invariant

        1, 4, 3, 0, 0, 0, x, ....
                 j        i
        i points to the first unprocessed element,
        j points to the first 0 element
        when nums[i] is 0 do nothing and increment i by 1
        when nums[i] is not 0, swap i, j and increment i, j by 1
        """
        i, j = 0, 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
