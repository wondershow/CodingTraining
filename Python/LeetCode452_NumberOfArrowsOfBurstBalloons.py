class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points = sorted(points, key = lambda p: (p[0], - p[1]))
        res, lo, hi = 1, points[0][0], points[0][1]
        for i in range(1, len(points)):
            lo1, hi1 = points[i][0], points[i][1]
            if lo1 > hi:
                res += 1
                lo, hi = lo1, hi1
            else:
                lo, hi = max(lo1, lo), min(hi1, hi)
        
        return res
