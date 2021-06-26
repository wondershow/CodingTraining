class Solution:
    """
    Dequeue
    Use a Deque to maintain a monotoically decreasing stack. Add from right, and pop from left.
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window, res = [], []
        for i in range(k):
            while window and window[-1][0] <= nums[i]:
                window.pop()
            window.append([nums[i], i])
        res.append(window[0][0])
        for i in range(k, len(nums)):
            while window and (window[-1][0] <= nums[i] or window[-1][1] + k <= i):
                window.pop()
            window.append([nums[i], i])
            while window and window[0][1] + k <= i:
                window.pop(0)
            res.append(window[0][0])
        return res
