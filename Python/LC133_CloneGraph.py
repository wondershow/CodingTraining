"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
Mistakes made:
1. Did not consider the edge case of empty tree
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        old_to_new = {}
        que, seen = [node], {node}
        while que:
            p = que.pop()
            new_p = Node(p.val)
            old_to_new[p] = new_p
            for nei in p.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    que.append(nei)
                    
        que, seen = [node], {node}
        
        while que:
            p = que.pop()
            for nei in p.neighbors:
                old_to_new[p].neighbors.append(old_to_new[nei])
                if nei not in seen:
                    seen.add(nei)
                    que.append(nei)
        
        return old_to_new[node]
