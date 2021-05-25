class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, N = [], len(nums)
        for i in range(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, N - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res
        
