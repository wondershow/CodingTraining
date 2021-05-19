class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, carry, res = len(num1) -1, len(num2) - 1, 0, []
        while i >= 0 or j >= 0:
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            tmp = a + b + carry
            res.append(str(tmp % 10))
            carry = tmp // 10
            i, j = i - 1, j - 1
        if carry == 1:
            res.append("1")
        res.reverse()
        return "".join(res)
