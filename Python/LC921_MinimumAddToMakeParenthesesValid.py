class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        balance, res = 0, 0
        for c in s:
            if c == "(":
                balance += 1
            elif c == ")":
                balance -= 1
                if balance < 0:
                    res += 1
                    balance = 0
        res += balance
        return res
