# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parent, y_parent, x_depth, y_depth = None, None, 0, 0
        def dfs(root, parent, x, y, depth):
            if not root:
                return
            nonlocal x_parent, y_parent, x_depth, y_depth
            if root.val == x:
                x_parent = parent
                x_depth = depth
            if root.val == y:
                y_parent = parent
                y_depth = depth
            dfs(root.left, root, x, y, depth + 1)
            dfs(root.right, root, x, y, depth + 1)
        
        dfs(root, None, x, y, 0)
        return x_depth == y_depth and x_parent != y_parent
