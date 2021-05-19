# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return [float("-inf"), 0]
            lres, max_to_l = helper(root.left)
            rres, max_to_r = helper(root.right)
            max_via_root = root.val
            if max_to_l > 0:
                max_via_root += max_to_l
            if max_to_r > 0:
                max_via_root += max_to_r
            local_max = max([lres, rres, max_via_root])
            return [local_max, root.val + max(0, max(max_to_l, max_to_r))]
        
        res, _ = helper(root)
        return res
