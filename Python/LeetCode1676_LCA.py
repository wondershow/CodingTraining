class Solution:
    '''
    DFS:
    1. report root if root is in nodes set since root is the LCA of the nodes rooted at root
    2. else traverse root's two children
    2.1 if both left and right are not none, still return root since root is a candidate of answer
    2.2 root is not a candidate, return l if l else r (best effort to return an non empty value)
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        expected = set(nodes)
        def helper(n):
            if not n:
                return None
            if n in expected:
                return n
            l = helper(n.left)
            r = helper(n.right)
            if l and r:
                return n
            return l if l else r
        return helper(root)
