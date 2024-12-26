class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        seen, total = Counter(nums), sum(nums)
        maxOutlier = float("-INF")
        for num in nums:
            if (total - num) % 2 == 0:
                if total - num != 2 * num and seen.get((total - num)// 2, 0) > 0:
                    maxOutlier = max(maxOutlier, num)
                elif total - num == 2 * num and seen.get((total - num)// 2, 0) > 1:
                    maxOutlier = max(maxOutlier, num)
        return maxOutlier
