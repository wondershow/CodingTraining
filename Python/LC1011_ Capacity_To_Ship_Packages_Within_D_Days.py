class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canship(capacity):
            days_needed, load = 1, 0
            for w in weights:
                load += w
                if load > capacity:
                    load, days_needed = w, days_needed + 1
            return days_needed <= days
            
        lo, hi = max(weights), sum(weights)
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if canship(mid):
                hi = mid
            else:
                lo = mid
        if canship(lo):
            return lo
        return hi
