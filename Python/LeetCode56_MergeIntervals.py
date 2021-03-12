class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res, lo, hi = [], intervals[0][0], intervals[0][0]
        for start, end in intervals:
            if hi < start:
                res.append([lo, hi])
                lo, hi = start, end
            else:
                hi = max(hi, end)
        res.append([lo, hi])
        return res
