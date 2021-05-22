# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        que = [root]
        while que:
            node = que.pop(0)
            if not node:
                break
            que.append(node.left)
            que.append(node.right)
            
        return not any(que)
