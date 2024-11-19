class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        We build a monotonic decreasing stack
        """
        stack = []
        for i, h in enumerate(heights):
            while stack and h >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack
