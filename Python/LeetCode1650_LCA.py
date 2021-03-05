"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    '''
        Roadmap:
        1. Find the height of both trees
        2. Move the taller one up until both nodes are at same height
        3. move both nodes up synchronously until they meet
    '''
    def lowestCommonAncestor1(self, p: 'Node', q: 'Node') -> 'Node':
        def height(n):
            res = 0
            while n:
                n = n.parent
                res += 1
            return res
        
        h1, h2 = height(p), height(q)
        if h1 < h2:
            p, q = q, p
            h1, h2 = h2, h1
        
        while h1 > h2:
            p = p.parent
            h1 -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p
    
    '''
    LinkedList converge point problem    
    '''
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, q1 = p, q
        while p1 != q1:
            p1 = p1.parent if p1.parent else q
            q1 = q1.parent if q1.parent else p
        return p1
