class TrieNode:
    def __init__(self):
        self.kids = {}

class Solution(object):
    def longestRepeatingSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        root = TrieNode()
        res = 0
        for start in range(len(s)):
            substr = s[start:]
            node, size = root, 0
            for c in substr:
                if c not in node.kids:
                    node.kids[c] = TrieNode()
                else:
                    size += 1
                node = node.kids[c]
            res = max(res, size)
        return res
                

