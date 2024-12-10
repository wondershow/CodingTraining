class Solution:
    
    """
    Greedy/Heuristic
    
    Scan from right to left, remember max_val, max_index
    when cur > max_val,
        update max_val and max_index
    when cur == max_val,
        do nothing
    when cur < max_val
         remember pair (cur_index, max_index)
    """
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        
        N = len(num)
        max_val, max_index, candidate_index = -1, -1, []
        i = N - 1
        while i >= 0:
            if int(num[i]) > max_val:
                max_index = i
                max_val = int(num[i])
            elif int(num[i]) < max_val:
                candidate_index = [max_index, i]
            i -= 1
        
        if not candidate_index:
            return int("".join(num))
        num[candidate_index[0]], num[candidate_index[1]] = num[candidate_index[1]], num[candidate_index[0]]
        return int("".join(num))

    def maximumSwap(self, num: int) -> int:
        """
        Scan from right to left, 
        we remember 1. maxIndex, maxVal
        2. at each iteration, if the currval is smaller than maxVal, update the swap index
        """
        i, arr = 0, [int(a) for a in str(num)]
        maxIndex, maxVal, candidate = len(arr) - 1, arr[-1], []
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > maxVal:
                maxVal = arr[i]
                maxIndex = i
            elif arr[i] < maxVal:
                candidate = [i, maxIndex]
        if not candidate:
            return num
        arr[candidate[0]], arr[candidate[1]] = arr[candidate[1]], arr[candidate[0]]
        return int("".join([str(a) for a in arr]))
