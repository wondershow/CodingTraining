class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo + k
    
    """
    define f(i) = arr[i] - (i + 1)
    The key is to find the index where f(i) < k and f(i + 1) >= k
    say the answer is M, which means f(M) < k, f(M + 1) >=k
    that means all k numbers after M will be missing, so M + K
    """
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr) - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if arr[mid] - (mid + 1) < k:
                lo = mid
            else:
                hi = mid
        #print("{} {}".format(lo, hi))
        if arr[lo] - (lo + 1) >= k:
            return lo + k
        elif arr[hi] - (hi + 1) >= k:
            return lo + k + 1
        return hi + k + 1
