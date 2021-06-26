# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Use the LC way to represent a binary tree (root, left, right)
    Do a post order traversal, at each node, compute subree rooted at that node. 
    If we see a duplicate, add it to the result. 
    """
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def helper(root, seen, res):
            if not root:
                return "#"
            left = helper(root.left, seen, res)
            right = helper(root.right, seen, res)
            sub_tree = str(root.val) + "," + left + "," + right
            if sub_tree in seen:
                res.append(seen[sub_tree])
            else:
                seen[sub_tree] = root
            return sub_tree
        
        res, seen = [], {}
        helper(root, seen, res)
        return list(set(res))
