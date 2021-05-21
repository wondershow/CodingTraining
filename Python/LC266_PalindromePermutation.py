class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = Counter(list(s))
        odd = 0
        for _, v in freq.items():
            if v % 2 == 1:
                odd += 1
        return odd < 2
