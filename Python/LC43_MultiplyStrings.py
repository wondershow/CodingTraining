class Solution:
    def multiply1(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        M, N = len(num1), len(num2)
        aux = [[0] * (M + N) for _ in range(N)]
        for j in range(N - 1, -1 , -1):
            row = offset = N - 1 - j
            carry = 0
            for i in range(M - 1, -1, -1):
                tmp = carry + int(num1[i]) * int(num2[j])
                aux[row][N - offset + i] = tmp % 10
                carry = tmp // 10
            aux[row][N - offset - 1] += carry
        res, carry = "", 0
        for i in range(M + N - 1, -1, -1):
            tmp = carry
            for row in range(N):
                tmp += aux[row][i]
            res = str(tmp % 10) + res
            carry = tmp // 10
        while res.startswith("0"):
            res = res[1:]
        return res
    """
    This method is much simpler.
    It uses the same idea, instead of using a 2d aux, we use a 1d aux.
    Just add single digit result into corresponding spot.
    """     
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        M, N = len(num1), len(num2)
        aux = [0] * (M + N)
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                aux[i + j + 1] += int(num1[i]) * int(num2[j])
        
        res, carry = "", 0
        for i in range(M + N - 1, -1, -1):
            tmp = carry + aux[i]
            res = str(tmp % 10) + res
            carry = tmp // 10
        
        while res.startswith("0"):
            res = res[1:]
        return res
        
