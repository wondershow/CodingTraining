class Solution:
    """
        The keys to solve this problem
        1. For a all nondecreasing sequence, there is no way to find a swap to get it smaller
        2. Scan from end to beigging, find first i that arr[i] > arr[i + 1], arr[i + 1:] is nondecreasing
        3. scan from i + 1 to end, find the smallest index of the largest number that is smaller than arr[i]
        swap i, j
           3.1 code see the implementation. 
        
        One more point is why do we need to scan from end to begining,
        that way we can make sure the leading part is unchanged, our change can only be the "Next" smaller/larger .....
    """
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        N = len(arr)
        i = N - 1
        while i > 0 and arr[i - 1] <= arr[i]:
            i -= 1
        if i == 0:
            return arr
        j = i
        right = -1
        while j < N:
            if arr[j] != arr[j - 1] and arr[j] < arr[i - 1]:
                right = j
            j += 1
        arr[i - 1], arr[right] = arr[right], arr[i - 1]
        return arr
        
