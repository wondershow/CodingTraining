# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def contains(self, node, r):
        if not node:
            return False
        if node == r:
            return True
        return self.contains(node.left, r) or self.contains(node.right, r)

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        pInLeft, qInLeft = self.contains(root.left, p), self.contains(root.left, q)
        if (pInLeft and not qInLeft) or (not pInLeft and qInLeft):
            return root
        if pInLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None

        # When returns true, it means the tree
        # roots at node contains at least one of p or q
        # We just need find the first node that left and right and itslef (2 out of 3 is true)
        def helper(node, p, q):
            nonlocal res
            if not node:
                return False
            left = helper(node.left, p, q)
            right = helper(node.right, p, q)
            mid = node == p or node == q
            if int(left) + int(right) + int(mid) == 2:
                res = node
            return left or right or mid
        
        helper(root, p, q)

        return res

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root in [p, q]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
