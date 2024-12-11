# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent, nodeByValue = {}, {}
        dq = deque()
        dq.append(root)
        while dq:
            node = dq.popleft()
            nodeByValue[node.val] = node
            if node.left:
                parent[node.left] = node
                dq.append(node.left)
            if node.right:
                parent[node.right] = node
                dq.append(node.right)
        dq.clear()
        dq.append(("", nodeByValue[startValue]))
        visited = set()
        visited.add(nodeByValue[startValue])
        while dq:
            path, node = dq.popleft()
            if node.val == destValue:
                return path
            if node.left and node.left not in visited:
                visited.add(node.left)
                dq.append((path + "L", node.left))
            if node.right and node.right not in visited:
                visited.add(node.right)
                dq.append((path + "R", node.right))
            if node in parent and parent[node] not in visited:
                visited.add(parent[node])
                dq.append((path + "U", parent[node]))
        return ""
