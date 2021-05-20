# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def helper(root, res, depth):
            if not root:
                return
            if len(res) == depth:
                res.append(root.val)
            helper(root.right, res, depth + 1)
            helper(root.left, res, depth + 1)
        res = []
        helper(root, res, 0)
        return res
