# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Build a graph, then bfs
    """
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = defaultdict(list)
        bfs, start = [root], None
        while bfs:
            parent = bfs.pop(0)
            if parent.val == k:
                start = parent
            if parent.left:
                graph[parent].append(parent.left)
                graph[parent.left].append(parent)
                bfs.append(parent.left)
            if parent.right:
                graph[parent].append(parent.right)
                graph[parent.right].append(parent)
                bfs.append(parent.right)
        
        seen, que = {start}, [start]
        while que:
            node = que.pop(0)
            if node.left == node.right == None:
                return node.val
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    que.append(neighbor)
        return -1
