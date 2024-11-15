# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return
            l_last, r_last = helper(node.left), helper(node.right)
            if l_last:
                l_last.right = node.right
                node.right = node.left
                node.left = None
            return r_last or l_last or node
        
        return helper(root)
