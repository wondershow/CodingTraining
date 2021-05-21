# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pre_val = [], float("-inf")
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre_val <= target < root.val:
                return min(pre_val, root.val, key=lambda x: abs(target - x))
            pre_val = root.val
            root = root.right
        return pre_val
        
    def closestValue1(self, root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            res = min(res, root.val, key = lambda x: abs(x - target))
            root = root.left if root.val > target else root.right
        return res
