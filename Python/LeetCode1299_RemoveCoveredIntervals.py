class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda v: (v[0], -v[1]))
        res, lo, hi = 1, intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            lo1, hi1 = intervals[i][0], intervals[i][1]
            if hi1 > hi:
                res += 1
                lo, hi = lo1, hi1
        return res
