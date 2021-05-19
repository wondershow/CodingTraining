"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    """
    Errors made:
    1. head, pre need to be declared as nonlocal in the helper method
    2. Edge case of empty tree
    3. pre.right not pre.'next'
    """
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head, pre = None, None
        def helper(root):
            nonlocal head, pre
            if not root:
                return
            helper(root.left)
            if not head:
                head = root
            root.left = pre
            if pre:
                pre.right = root
            pre = root
            helper(root.right)
        if not root:
            return root
        helper(root)
        head.left = pre
        pre.right = head
        return head
                
