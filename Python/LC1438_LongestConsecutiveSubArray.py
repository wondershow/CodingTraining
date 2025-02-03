from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increase, decrease = deque(), deque()
        right, N = 1, len(nums)
        increase.append(nums[0])
        decrease.append(nums[0])
        res = 1
        for i in range(N):
            while right < N and decrease[0] - increase[0] <= limit:
                while decrease and nums[right] > decrease[-1]:
                    decrease.pop()
                decrease.append(nums[right])
                while increase and nums[right] < increase[-1]:
                    increase.pop()
                increase.append(nums[right])
                right += 1
                if decrease[0] - increase[0] <= limit:
                    res = max(res, right - i)
            if nums[i] == increase[0]:
                increase.popleft()
            if nums[i] == decrease[0]:
                decrease.popleft()
        return res
