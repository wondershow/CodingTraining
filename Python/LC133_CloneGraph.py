"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    This is a one pass BFS solution. 
    We use a mapping 'visited' to keep mapping from old to new node
    During BFS, whenever we want to add a node to the bfs que, it is time to clone that node to put in the visited mapping.
    Meanwhile, when we are iterating one nodes neighbor, we add the neighbor's clone to node's clone's neighbor list.
    The reason is that we iterate each edge exactly 2 times. one time b is a's neigbor, the other time a is b's neighbor.
    
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        seen, visited = {node}, {node : Node(node.val, [])}
        que = [node]
        while que:
            n = que.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    que.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
