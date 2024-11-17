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

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Scan from left to right until 2*N
        keep montonic non-increasing (note not "decreasing" as there might be duplicates,
        when there is a duplicate, both items should be in the stack) stack. 
        At each position, to keep the monotocity if an old stack popped (say this is x), x's first 
        big element on the right is cur item.
        some points:
        1. We iterate 2 * N to meet the "circular".
        2. When we hit the max value after N, break.
        3. in the stack we store the index not the actual value. 
        """

        N = len(nums)
        stack, res, max_ele = [], [-1] * N, nums[0]
        for i in range(2 * N):
            num = nums[i % N]
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i % N)
            max_ele = max(num, max_ele)
            if i >= N and num == max_ele:
                break
        return res
