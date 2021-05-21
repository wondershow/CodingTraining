# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    The helper does one thing, it tells if that tree contains p or q or their ancesor
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root:
                return None
            if root in [p, q]:
                return root
            l = helper(root.left, p, q)
            r = helper(root.right, p, q)
            if not l:
                return r
            if not r:
                return l
            return root
        
        return helper(root, p, q)
