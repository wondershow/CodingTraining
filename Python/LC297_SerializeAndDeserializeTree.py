# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root, res):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            helper(root.left, res)
            helper(root.right, res)
        
        res = []
        helper(root, res)
        while res and res[-1] == "#":
            res.pop()
        return ",".join(res)
        

    def deserialize(self, input_value):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not input_value:
            return None
        
        values = input_value.split(",")
        index = 0
        def builder(data):
            nonlocal index
            if index >= len(data) or data[index] == "#":
                index += 1
                return None
            root = TreeNode(int(data[index]))
            index += 1
            root.left = builder(data)
            root.right = builder(data)
            return root
        return builder(values)
