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

    class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        This seems to be much easire and efficient.
        We first use backtracking to get the path from root to both nodes
        Then find the LCA (using both path). 
        from start node, we do "U", from LCA to dest, we use the path as is.
        """
        def getPath(node, target, path):
            if not node:
                return False
            if node.val == target:
                return True
            path.append("L")
            if getPath(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if getPath(node.right, target, path):
                return True
            path.pop()

        rootToStart, rootToDest = [], []
        getPath(root, startValue, rootToStart)
        getPath(root, destValue, rootToDest)
        index = 0
        while index < min(len(rootToStart), len(rootToDest)):
            if rootToStart[index] != rootToDest[index]:
                break
            index += 1
        return "U" * (len(rootToStart) - index) + "".join(rootToDest[index:])
