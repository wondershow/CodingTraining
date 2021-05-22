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
