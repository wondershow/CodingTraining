# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        def dfs(root, res, depth):
            if not root:
                return
            if len(res) == depth:
                res.append(root.val)
            else:
                res[depth] = max(res[depth], root.val)
            dfs(root.left, res, depth + 1)
            dfs(root.right, res, depth + 1)
        res = []
        dfs(root, res, 0)
        return res
