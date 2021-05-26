# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre_val = float("-inf")
        stack, p = [], root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if p.val <= pre_val:
                return False
            pre_val = p.val
            p = p.right
        return True
