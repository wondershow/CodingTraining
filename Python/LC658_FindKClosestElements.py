class Solution:
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            
            """
            hit the nail on the head. This is actually how the correct solution is hard to devise here. 
            It is designed to compare two windows every time, which is not finding lower bound/upper bound or the exact point like what binary search is usually doing.
            
            
            at each mid position we guess [mid: mid + k] (not arr[mid + k] is not in this window)
            we have two windows here w1 : [mid: mid + k] ( ending at arr[mid + k - 1])
                                     w2 : [mid + 1, mid + k + 1] (ending at arr[mid + k])
                                     
            w1:       A[mid], A[mid + 1], ..., A[mid + k - 1]
            w2:               A[mid + 1], ..., A[mid + k - 1], A[mid + k]
            moving right means making the situation worse (the if condition), so we exclude right half search space.                          
                            
            the if comparison is to compare if w2 window (moving right wards) can find a better solution, if <=, that means movign rightwards 
            only enlarges the gap, so we need to exclude that half soltuion
            """
            if x - arr[mid] <= arr[mid + k] - x:
                hi = mid
            else:
                lo = mid + 1
        return arr[lo:lo + k]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
            if len(arr) == k:
                return arr
            lo, hi = 0, len(arr) - k
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if x - arr[mid] <= arr[mid + k] - x:
                    hi = mid
                else:
                    lo = mid
            if x - arr[lo] <= arr[lo + k] - x:
                return arr[lo : lo + k]
            return arr[hi : hi + k]
