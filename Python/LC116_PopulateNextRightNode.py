"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(root, parent):
            if not root:
                return
            if parent:
                if root == parent.left:
                    root.next = parent.right
                elif parent.next:
                    root.next = parent.next.left
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root, None)
        return root
