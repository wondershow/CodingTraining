class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        last = self.countAndSay(n - 1) + " "
        count, val = 1, last[0]
        res = ""
        for i in range(1, len(last)):
            if last[i] == last[i - 1]:
                count += 1
            else:
                res += str(count) + last[i - 1] 
                count = 1
        return res
