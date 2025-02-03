class Solution:
    """
    1. Build a tree (node => kids mapping)
    2. post order access each node, 
       2.1 update longest path ending at current node
       2.2 If possible update longest path going from a kid to this node to another kid
    """
    def longestPath(self, parent: List[int], s: str) -> int:
        res = 1
        def dfs(node):
            nonlocal res
            top2Kids = []
            for kid in kids[node]:
                dfs(kid)
                if s[node] != s[kid]:
                    maxEndingAt[node] = max(maxEndingAt[node], maxEndingAt[kid] + 1)
                    bisect.insort(top2Kids, maxEndingAt[kid])
                    if len(top2Kids) > 2:
                        top2Kids.pop(0)
            if top2Kids:
                res = max(1 + sum(top2Kids), res)
        
        kids = defaultdict(list)
        N = len(s)
        root = -1
        for kid, parent in enumerate(parent):
            if parent != -1:
                kids[parent].append(kid)
            else:
                root = kid
        maxEndingAt = [1 for i in range(N)]
        dfs(root)
        return res
        
        
        
