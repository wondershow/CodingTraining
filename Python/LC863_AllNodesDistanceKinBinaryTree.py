# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
the if depth > k:
                break
                statement should be put before the for loop.
"""
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def build_graph(root, res):
            if not root:
                return
            if root.left:
                res[root].append(root.left)
                res[root.left].append(root)
                build_graph(root.left, res)
            if root.right:
                res[root].append(root.right)
                res[root.right].append(root)
                build_graph(root.right, res)
        
        graph = defaultdict(list)
        build_graph(root, graph)
        #print(graph)
        que, res, seen, depth = [target], [], {target}, 0
        while que:
            size = len(que)
            if depth > k:
                break
            for _ in range(size):
                node = que.pop(0)
                if depth == k:
                    res.append(node.val)
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        que.append(nei)
            depth += 1
        return res
