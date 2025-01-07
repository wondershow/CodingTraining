class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res, s, e = [], toBeRemoved[0], toBeRemoved[1]
        for start, end in intervals:
            if max(start, s) < min(end, e):
                if start < s:
                    res.append([start, s])
                if end > e:
                    res.append([e, end])
            else:
                res.append([start, end])
        return res
