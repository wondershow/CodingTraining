class Trie:
    def __init__(self):
        self.kids = {}

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def build_trie(arr):
            root = Trie()
            for number in arr1:
                node = root
                for c in list(str(number)):
                    if c not in node.kids:
                        node.kids[c] = Trie()
                    node = node.kids[c]
            return root
        
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        root, res = build_trie(arr1), 0
        for number in arr2:
            node, depth = root, 0
            for c in list(str(number)):
                if c not in node.kids:
                    break
                node = node.kids[c]
                depth += 1
            res = max(res, depth)
        return res
