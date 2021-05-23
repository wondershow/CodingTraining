# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    A stack based method
    The key is we have a read_val method to read next number and move cursor.
    Always move "(num" in pair and push it into stack. When we see a ")" then pop
    when poping a node out from stack, its parent is the new stack top (if stack not empty).
    so we use a flag [node, flag] to pass into the stack to indicate if the left child of that node has been set.
    """
    def str2tree(self, s: str) -> TreeNode:
        def read_val(s):
            nonlocal index
            val, negative = 0, 1
            if s[index] == "-":
                negative, index = -1, index + 1
            while index < len(s) and s[index].isdigit():
                val = val * 10 + int(s[index])
                index += 1
            return val * negative
        
        if not s:
            return None
        
        index = 0
        root = TreeNode(read_val(s))
        stack = [[root, True]]
        while index < len(s):
            if s[index] == "(":
                index += 1
                node = TreeNode(read_val(s))
                if stack[-1][1]:
                    stack[-1][0].left = node
                    stack[-1][1] = False
                else:
                    stack[-1][0].right = node
                stack.append([node, True])
            elif s[index] == ")":
                stack.pop()
                index += 1
                
        return root
