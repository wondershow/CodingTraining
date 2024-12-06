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
    Define: S (1,2,3,4,...M), we have (M - k) elements in the arr, then M is the kth missing element.

    Define: f(i) = arr[i] - (i + 1)
    Explaination: f(i) is the number of missing numbers that arr[:(i + 1)] has

    1. when f(i) is smaller than k, that means to find S, we have to increase i to the right of the arr.
    2. when f(i - 1) < k and f(i) >= k meaning, arr[:(i + 1)] misses equal or more than k numbers. 
        Therefore we have 1,2,3,4,..M,..., arr[i] (note that arr[i] might be equal to M)
        Since we are confident that arr[0...(i - 1)] (all together i numbers) present in our (1,2,...M) sequence, note that M is the Kth missing number. So we can say i + k = M so we find M.
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
