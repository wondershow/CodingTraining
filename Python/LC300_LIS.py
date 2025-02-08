class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis, N = [], len(nums)
        for i in range(0, N):
            pos = bisect_left(lis, nums[i])
            if pos == len(lis):
                lis.append(nums[i])
            else:
                lis[pos] = nums[i]
        return len(lis)
