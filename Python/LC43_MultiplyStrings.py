class Solution:
    """
    Mistakes made at the comment
    """
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        M, N = len(num1), len(num2)
        if M < N:
            return self.multiply(num2, num1)
        
        res = [[0] *  (M + N) for _ in range(N)]
        
        for i in range(N - 1, -1, -1):
            right, carry, factor = M + i, 0, int(num2[i])
            for j in range(M - 1, -1, -1):
                tmp = int(num1[j]) * factor + carry
                res[i][right] = tmp % 10
                carry = tmp // 10
                right -= 1
            res[i][right] = carry
        
        ret, carry = "", 0
        for i in range(M + N - 1, -1, -1):
            tmp = carry
            for j in range(N):
                tmp += res[j][i]
                
            # Mistake made here.
            ret = str(tmp % 10) + ret
            carry = tmp // 10
        
        if ret.startswith("0"):
            ret = ret[1:]
        return ret
                
                
