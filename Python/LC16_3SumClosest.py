def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N, best = len(nums), float("inf")
        for i in range(N - 2):
            l, r = i + 1, N - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total
                if abs(total - target) < abs(best - target):
                    best = total
                if total < target:
                    l += 1
                else:
                    r -= 1
        return best
