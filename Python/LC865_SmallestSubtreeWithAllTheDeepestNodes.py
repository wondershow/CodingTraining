# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return [None, 0]
            lres, ldepth = dfs(root.left)
            rres, rdepth = dfs(root.right)
            if ldepth > rdepth:
                return [lres, ldepth + 1]
            if ldepth < rdepth:
                return [rres, rdepth + 1]
            return [root, rdepth + 1]
        
        return dfs(root)[0]
