class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        N = len(nums)

        '''
        left[i] = a means the subarray nums[a : i + 1] with nums[i] as the minimum value
        right[i] = a means the subarray nums[i : a + 1] with nums[i] as the minimum value

        To populate the left array, scan left to right, keep a montonic incresing stack,
        Before an element (cur) is pushed into stack, all the poped index's value is larger than the cur, so we keep left[cur_index] = left[stack.pop()] (this traces back to 1st position of repeated item)
        '''
        left, right = [i for i in range(N)], [i for i in range(N)]
        stack = []
        for i in range (N):
            while stack and nums[stack[-1]] >= nums[i]:
                left[i] = left[stack.pop()]
            stack.append(i)
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                right[i] = right[stack.pop()]
            stack.append(i)
        
        for i in range(N):
            k = right[i] - left[i] + 1
            if nums[i] > threshold / k:
                return k
        return -1
