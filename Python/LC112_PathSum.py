# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        res = False
        def dfs(root, remains):
            if not root:
                return
            remains -= root.val
            nonlocal res
            if res or root.left == root.right == None and remains == 0:
                res = True
                return
            dfs(root.left, remains)
            dfs(root.right, remains)
        dfs(root, targetSum)
        return res
