class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum, running = [], 0
        for i in w:
            running += i
            self.prefix_sum.append(running)
    
    """
    This binary search is ugly, need to improve it.
    """
    def pickIndex(self) -> int:
        pick = random.randint(1, self.prefix_sum[-1])
        lo, hi = 0, len(self.prefix_sum) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if self.prefix_sum[mid] <= pick:
                lo = mid
            else:
                hi = mid
        if self.prefix_sum[lo] < pick <= self.prefix_sum[hi]:
            return hi
        return lo
