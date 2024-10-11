class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        This is a nasty (no pattern problem). 3 steps
        1. Scan from right to left, find 1st positon (beta) which is larger than its prev (alpha)
        2. Scan from beta, find last position that is larger than alpha, swap it with alpha
        3. reverse from beta to end
        
        Reasoning:
        When find last increasing neighbor(say A and B), this is where we could find a "next" big number becase there is a disorder here. 
        The problems is what the leading number after the adjustment. We need to find the elments after B that is smallest but largther than A, say C. C should be the leading number with smallest order. We swap C and A. Then from B to end of the array is decresing order, which is not small enough. We reverse them. 
        """
        last_increase_pos = len(nums) - 1
        while last_increase_pos > 0:
            if nums[last_increase_pos] > nums[last_increase_pos - 1]:
                break
            last_increase_pos -= 1
        if last_increase_pos == 0:
            nums.reverse()
            return

        i, N = last_increase_pos, len(nums)
        while i < N and nums[i] > nums[last_increase_pos - 1]:
            i += 1

        nums[i - 1], nums[last_increase_pos - 1] = nums[last_increase_pos - 1], nums[i - 1]

        lo, hi = last_increase_pos, N - 1
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo, hi = lo + 1, hi - 1
