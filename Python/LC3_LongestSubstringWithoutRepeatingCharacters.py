class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, res, j, N = set(), 0, 0, len(s)
        for i, c in enumerate(s):
            while j < N:
                if s[j] in seen:
                    break
                seen.add(s[j])
                j += 1
            res = max(j - i, res)
            seen.remove(c)
        return res
