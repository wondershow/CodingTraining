class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N == 1:
            return
        i = N - 1
        
        ## Need to carefully inspect the position of i after loop
        ## In this case, it points to the larger element on the right
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        j = i
        while j < N and nums[j] > nums[i - 1]:
            j += 1
        nums[i - 1], nums[j - 1] = nums[j - 1], nums[i - 1]
    
        lo, hi = i, N - 1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo + 1, hi - 1
