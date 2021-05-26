class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_up(piles, k, h):
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            return time <= h
        
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_eat_up(piles, mid, h):
                hi = mid
            else:
                lo = mid + 1
        return lo
