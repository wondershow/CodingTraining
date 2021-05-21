class Solution:
    """
    To solve this problem, we need to use "Binary search" and carefully inspect edge cases:
    Use addition to duplicate addtion factor by 2 each time so that we can quickly approach dividend in 
    log time. Only reach stricly lower bound and recursively call to get the missing factor
    Edge case:
    1. dividend is 0 
    2. dividend is MAX_INT and divisor = 1 or dividend is MIN_INT and divisor = -1
    3. dividend < divisor
    
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == 2**31 and divisor == 1 or dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        negative = False
        if dividend > 0 and divisor < 0 or divisor > 0 and dividend < 0:
            negative = True
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        
        quotient, running_sum = 1, divisor
        while running_sum  + running_sum < dividend:
            running_sum += running_sum
            quotient += quotient
            
        res = quotient + self.divide(dividend - running_sum, divisor)
        if negative:
            return -res
        return res
