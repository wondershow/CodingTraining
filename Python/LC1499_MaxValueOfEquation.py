class Solution:
    """
    Since the input is already sorted by x values. 
    When we scan from left to right, |xi - xj| = xi - xj (xi is the current pos) 
    so yi + yj + |xi - xj| = (xi + yi) + (yj - xj)
    At each iteration, we just need to find max(yj - xj) for all previous points which meet the 
    condition |xi - xj| <= k
    """
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap = []
        res = float("-inf")
        for x, y in points:
            while heap and heap[0][1] + k < x:
                heappop(heap)
            if heap:
                res = max(res, x + y - heap[0][0])
            heappush(heap, [x - y, x])
        return res
