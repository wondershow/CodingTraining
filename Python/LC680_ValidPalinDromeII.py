class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(s, left, right, erasure):
            while left < right:
                if s[left] != s[right]:
                    if not erasure:
                        return False
                    return helper(s, left + 1, right, False) or helper(s, left, right - 1, False)
                left, right = left + 1, right - 1
            return True
        return helper(s, 0, len(s) - 1, True)
