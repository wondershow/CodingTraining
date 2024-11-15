# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def preOrder(node, parent_val, length):
            if not node:
                return
            nonlocal max_len
            if node.val == parent_val + 1:
                length += 1
            else:
                length = 1
            max_len = max(max_len, length)
            preOrder(node.left, node.val, length)
            preOrder(node.right, node.val, length)

        preOrder(root, float("-INF"), 0)
        return max_len
