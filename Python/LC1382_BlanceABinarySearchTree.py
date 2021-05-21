# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def build(nodes, lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = nodes[mid]
            root.left = build(nodes, lo, mid - 1)
            root.right = build(nodes, mid + 1, hi)
            return root
        
        nodes, stack, p = [], [], root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            nodes.append(p)
            p = p.right
            
        return build(nodes, 0, len(nodes) - 1)
