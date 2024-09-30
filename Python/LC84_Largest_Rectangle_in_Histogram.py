class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # We need a monotically increasing stack of (index) to track the elements 
        # on the left of current position.
        # Scan from left to right, pop out stack when stack top is smaller 
        # or equal than cur. The computation/comparison happens at each popped
        # out element. For each popped out element, the largests rectangle ='s left boundary is the new stack top (not included)
        # right boundary is the cur (not included). Also we need to make sure all original items are compared when the scanning is done, so we sandwich the original heights array with two additional 0's.
        max_area, stack, heights = 0, [], [0] + heights + [0]
        for i, h in enumerate(heights):
            max_area = max(max_area, h)
            while stack and h < heights[stack[-1]]:
                index = stack.pop()
                h1 = heights[index]
                if stack:
                    area = (i - stack[-1] - 1) * h1
                    max_area = max(area, max_area)
            stack.append(i)
        return max_area
