class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        N = len(height)
        left, right = [0] * N, [0] * N
        left[0], right[N - 1] = height[0], height[N - 1]
        for i in range(1, N):
            left[i] = max(height[i], left[i - 1])
        for i in range(N - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        res = 0
        for i in range(1, N - 1):
            res += max(0, min(left[i - 1], right[i + 1]) - height[i])
        return res
