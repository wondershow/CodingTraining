class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        def is_under_budget(val):
            """
            A dumb question. More like a math brain teaser than an algrotim problem.
            Need to use your pen to do some math formulation
            """
            budget = 0
            if val > index:
                budget += (val + val - index) * (index + 1) / 2
            else:
                budget += (1 + val) * val / 2 + index - val + 1

            if val >= n - index:
                budget += (val + val - n + index) * (n - index - 1) / 2
            else:
                budget += val * (val - 1) / 2 + n - index - val

            return budget <= maxSum
        lo, hi = 0, maxSum
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if is_under_budget(mid):
                lo = mid
            else:
                hi = mid
        if is_under_budget(hi):
            return hi
        return lo
        
