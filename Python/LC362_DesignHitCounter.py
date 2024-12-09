class HitCounter:

    def __init__(self):
        self.timestamps = []

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if not self.timestamps:
            return 0
        lo, hi = 0, len(self.timestamps) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if self.timestamps[mid] <= timestamp - 300:
                lo = mid
            else:
                hi = mid
        if self.timestamps[lo] > timestamp - 300:
            start = lo
        elif self.timestamps[hi] > timestamp - 300:
            start = hi
        else:
            start = hi + 1
        return len(self.timestamps) - start


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
