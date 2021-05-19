class Solution:
    """
    Sort of "O(1)" space.
    store temp results in the returned variable
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, running = [1], 1
        for num in nums:
            running *= num
            res.append(running)
        N, running = len(nums), 1
        for i in range(N - 1, -1, -1):
            res[i + 1] = res[i] * running
            running *= nums[i]
        res.pop(0)
        return res
