# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def helper(node):
            nonlocal max_len
            incr, decr = 1, 1
            if node.left:
                l_incr, l_decr = helper(node.left)
                if node.val == node.left.val + 1:
                    incr = l_incr + 1
                if node.val == node.left.val - 1:
                    decr = l_decr + 1
            if node.right:
                r_incr, r_decr = helper(node.right)
                if node.val == node.right.val + 1:
                    incr = max(incr, r_incr + 1)
                if node.val == node.right.val - 1:
                    decr = max(decr, r_decr + 1)
            max_len = max(max_len, decr + incr - 1)
            return [incr, decr]
