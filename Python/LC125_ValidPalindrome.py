class Solution:
    """
    The while loop needs to do manual increment and decrement
    """
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if l < r and s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
