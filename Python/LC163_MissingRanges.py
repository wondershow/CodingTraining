class Solution:
    """
    Mistakes made:
    1. Failed to update "expected" at EVERY iteration (not some iterations)
    """
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        expected, res = lower, []
        nums.append(upper + 1)
        for num in nums:
            if expected < num - 1:
                res.append(str(expected) + "->" + str(num - 1))
            elif expected == num - 1:
                res.append(str(expected))
            
            expected = num + 1
        """
        if expected < upper - 1:
            res.append(str(expected) + "->" + str(upper - 1))
        elif expected == upper - 1:
            res.append(str(expected))
        """
        return res
