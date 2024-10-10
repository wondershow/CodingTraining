class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        We scan from right (index 2N) to left and build keep a monotonic decreasing stack.
        At each positioin, we adjust the stack (pop the stack until the cur is >= stack top),
        then the new stacktop is the "next greater element" of the cur. 
        At end of iteration, we push the cur item to the stack.
        """
      
        stack, N = [], len(nums)
        map_next_greater = {}
        for i in range(2 * N - 1, -1, -1):
            while stack and nums[stack[-1] % N] <= nums[i % N]:
                stack.pop()
            if stack:
                map_next_greater[i] = nums[stack[-1] % N]
            else:
                map_next_greater[i] = -1
            stack.append(i)

        return [map_next_greater[i] for i in range(N)]
