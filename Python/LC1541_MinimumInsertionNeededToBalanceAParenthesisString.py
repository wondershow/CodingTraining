class Solution:
    """
    we keep a balance variable and scan s (use while)
    when it is open add balance by 2
    when it is close, check if the next two (mind boundary) are both closes, 
        if both close, reduce balance by 2
        if not, we need one insertion of ")" to make this close to be a pair
        update balance
    in each iteration, inspect balance, whenever it is negative, an insertion of "(" is needed to make balance positive.
    
    when scan is over, add balance to res
    """
    def minInsertions(self, s: str) -> int:
        count, res = 0, 0
        N, i = len(s), 0
        while i < N:
            if s[i] == "(":
                count += 2
                i += 1
            elif i < N - 1 and s[i + 1] == s[i] == ")":
                count -= 2
                i += 2
            else:
                res += 1
                count -= 2
                i += 1
            if count < 0:
                res += (-count + 1) // 2
                count = 0 if count % 2 == 0 else 1
        
        return res + count
                
