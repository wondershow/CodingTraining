class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res, s, e = [], newInterval[0], newInterval[1]
        for start, end in intervals:
            if start > e or end < s:
                res.append([start, end])
            else:
                s, e = min(s, start), max(e, end)
        bisect.insort(res, [s, e])
        return res
