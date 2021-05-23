# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return [True, 0, float("inf"), float("-inf")]
            lres, lsize, lmin, lmax = helper(root.left)
            rres, rsize, rmin, rmax = helper(root.right)
            if lres and rres and lmax < root.val < rmin:
                lmin = lmin if lmin != float("inf") else root.val
                rmax = rmax if rmax != float("-inf") else root.val
                return [True, lsize + rsize + 1, lmin, rmax]
            return [False, max(lsize, rsize), float("inf"), float("-inf")]
        
        
        return helper(root)[1]
                
                
