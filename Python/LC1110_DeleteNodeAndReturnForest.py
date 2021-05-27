# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        """
        It is tricky. At each node, we need to know its parent to decide if this node 
        will be the new root (parent is none and this node is not to be deleted).
        Mean while, we need to return current node as None if it is to be deleted
        """
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def dfs(root, to_delete, parent, res):
            if not root:
                return None
            new_root = None if root.val in to_delete else root
        
            root.left = dfs(root.left, to_delete, new_root, res)
            root.right = dfs(root.right, to_delete, new_root, res)
            
            if not parent and root.val not in to_delete:
                res.append(root)
            return new_root
        res = []
        dfs(root, set(to_delete), None, res)
        return res
