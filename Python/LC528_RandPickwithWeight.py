class Solution_2021:

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


class Solution_2024:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0] * len(w)
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = w[i] + self.prefix_sum[i - 1]

    def pickIndex(self) -> int:
        pick = random.randint(1, self.prefix_sum[-1])

        # If we can use bisect
        # return bisect_left(self.prefix_sum, pick)

        # home brew bisect
        lo, hi = 0, len(self.prefix_sum) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if self.prefix_sum[mid] < pick:
                lo = mid
            else:
                hi = mid
        if self.prefix_sum[lo] >= pick:
            return lo
        return hi
