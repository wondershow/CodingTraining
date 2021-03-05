class Solution:
    '''
    Find LCA and then use BFS to compute distance to both nodes
    '''
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def findLCA(n, p, q):
            if not n:
                return None
            if n.val in [p, q]:
                return n
            l = findLCA(n.left, p, q)
            r = findLCA(n.right, p, q)
            if l and r:
                return n
            return l if l else r
        
        res, depth = 0, 0
        que = [findLCA(root, p, q)]
        while que:
            for _ in range(len(que)):
                n = que.pop(0)
                if n.val in [p, q]:
                    res += depth
                if n.left:
                    que.append(n.left)
                if n.right:
                    que.append(n.right)
            depth += 1
        return res
