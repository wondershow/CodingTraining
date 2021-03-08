# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        swap, prev = [], None
        
        def helper(root, swap):
            nonlocal prev
            if not root:
                return
            helper(root.left, swap)
            if prev and root.val <= prev.val:
                if not swap:
                    swap.extend([prev, root])
                else:
                    swap[-1] = root
            prev = root
            helper(root.right, swap)
            
        helper(root, swap)
        if swap:
            swap[0].val, swap[1].val = swap[1].val, swap[0].val 
