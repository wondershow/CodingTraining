# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(root, res):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            dfs(root.left, res)
            dfs(root.right, res)
        
        res = []
        dfs(root, res)
        while res and res[-1] == "#":
            res.pop()
        return ".".join(res)
                

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(values):
            nonlocal index
            if index >= len(values):
                return None
            if values[index] == "#":
                index += 1
                return None
            root = TreeNode(int(values[index]))
            index += 1
            root.left = helper(values)
            root.right = helper(values)
            return root
        
        if not data:
            return None
        values = data.split(".")
        index = 0
        return helper(values)
