class Solution:
    """
    Just follow the statements.
    """
    def myAtoi(self, s: str) -> int:
        val, index, N = 0, 0, len(s)
        factor = 1
        while index < N and s[index] == ' ':
            index += 1
        if index == N:
            return val
        if s[index] in "+-":
            if s[index] == "-":
                factor = -1
            index += 1
        if index == N:
            return val
        while index < N and s[index].isdigit():
            val = 10 * val + int(s[index])
            index += 1
        
        val = val * factor
        if val < -2**31:
            val = -2**31
        if val >= 2**31:
            val = 2**31 - 1
        return val
