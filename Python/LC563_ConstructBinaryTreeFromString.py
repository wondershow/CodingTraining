# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def read(s):
            nonlocal index
            val, sign = 0, 1
            if s[index] == "-":
                sign = -1
                index += 1
            while index < len(s) and s[index].isdigit():
                val = val * 10 + int(s[index])
                index += 1
            return val * sign
        
        if not s:
            return None
        index = 0
        root = TreeNode(read(s))
        stack = [[root, True]]
        while index < len(s):
            if s[index] == "(":
                index += 1
                node = TreeNode(read(s))
                stack.append([node, True])
            else:
                index += 1
                node, _ = stack.pop()
                if stack[-1][1]:
                    stack[-1][0].left = node
                    stack[-1][1] = False
                else:
                    stack[-1][0].right = node
        return root
