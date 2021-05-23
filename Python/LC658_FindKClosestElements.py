class Solution:
    
    """
    Not sure how this binary search model works. But need to be aware that
    in the while loop, we group if '<=' condition with hi = mid, that way we wont miss the condition where the mid point meets the condition f[x] = what we need. 
    """
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k
        while lo < hi:
            mid = (lo + hi) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                hi = mid
            else:
                lo = mid + 1
            
        return arr[lo:lo + k]
