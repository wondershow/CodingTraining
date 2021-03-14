class Solution:
    '''
    DP method, TLE. The Java version can pass because Java is more efficient than Python.
    '''
    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        """
        dp[i] is the maximum non-overlapping intervals in the from 0  to i-1 items
        """
        if not intervals:
            return 0
        
        N = len(intervals)
        intervals.sort()
        dp = [1] * N
        for i in range(1, N):
            s1, e1 = intervals[i][0], intervals[i][1]
            for j in range(i):
                s2, e2 = intervals[j][0], intervals[j][1]
                if e2 <= s1 or e1 <= s2:
                    dp[i] = max(dp[i], dp[j] + 1)
        return N - dp[-1]
    
    """
    A greedy method. I did not come up with it but coded it up after reading the solution.
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        N = len(intervals)
        
        # res is the number of intervals in the longest non overlapping set
        res, prev = 1, 0
        intervals.sort()
        
        for i in range(1, N):
            s1, e1 = intervals[prev][0], intervals[prev][1]
            s2, e2 = intervals[i][0], intervals[i][1]
            if e1 <= s2:
                res += 1
                prev = i
            elif e2 < e1:
                prev = i
        
        return N - res
                
