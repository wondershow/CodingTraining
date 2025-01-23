class Solution:
    def isPowerOfTwo1(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 ==0:
            n = n // 2
        return n == 1

    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        return n & ( n - 1) == 0

    
        
