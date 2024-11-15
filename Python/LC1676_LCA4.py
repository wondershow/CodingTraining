# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        res = None
        def helper(node, targets):
            nonlocal res
            if not node:
                return False
            mid = node in targets
            left, right = helper(node.left, targets), helper(node.right, targets)
            if int(mid) + int(left) + int(right) >= 2:
                res = node
            return mid or left or right
        if len(nodes) == 1:
            return nodes[0]
        helper(root, set(nodes))
        return res
