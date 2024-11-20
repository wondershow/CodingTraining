class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Watchout for the range of for loop.
        """
        N = len(nums)
        answer = 0
        cur_end, cur_max = 0, 0
        for i in range(N - 1):
            cur_max = max(cur_max, i + nums[i])
            if i == cur_end:
                answer += 1
                cur_end = cur_max
        return answer
