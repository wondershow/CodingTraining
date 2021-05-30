class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix = [0]
        for a in w:
            self.prefix.append(self.prefix[-1] + a)
        self.prefix.pop(0)
    """
    e.g. w = [1,2,3,4]
    prefix = [1, 3, 6, 10]
    the rand number has to be 1 ~ 10
    0 ~ 9 is a hassel
    """
    def pickIndex(self) -> int:
        rand_val = random.randint(1, self.prefix[-1])
        lo, hi = 0, len(self.prefix) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.prefix[mid] < rand_val:
                lo = mid + 1
            else:
                hi = mid
        return lo
