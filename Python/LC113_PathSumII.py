# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Mistakes made
    1. Failed to do path.pop()/backtracking before 1st return statement
    """
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, res, path, remains):
            path.append(root.val)
            remains -= root.val
            if not root.left and not root.right:
                if remains == 0:
                    res.append(list(path))
                path.pop()
                return
            if root.left:
                dfs(root.left, res, path, remains)
            if root.right: 
                dfs(root.right, res, path, remains)
            path.pop()
        if not root:
            return[]
        res = []
        dfs(root, res, [], targetSum)
        return res
