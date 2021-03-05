class Solution:
    '''
    Use a global variable res.
    DFS:
        rate each node, if 
        +1 if left tree contains p or q or both
        +1 if right tree contains p or q or both
        +1 if root is p or q or both
        assign root to res when
        1. res is not assigned any value yet (it is "None")
        2. rating of a node is 2
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def helper(root, p, q):
            nonlocal res
            if not root:
                return False 
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)
            mid = root in [p, q]
            if left + right + mid == 2:
                res = root
            return left or right or mid
        helper(root, p, q)
        return res
