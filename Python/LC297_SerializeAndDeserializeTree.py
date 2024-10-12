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

        For this problem, we use preorder output plus all the empty leaves (#) to serilize a tree.
        Whenenver there is a #, that means a child tree travels to the end. I think my explaination is not 
        very convincing.
        """
        def preorder(node, path):
            if not node:
                path.append("#")
                return
            path.append(str(node.val))
            preorder(node.left, path)
            preorder(node.right, path)
        path = []
        preorder(root, path)
        return " ".join(path)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        index = 0

        def build_tree(values):
            nonlocal index
            if values[index] == '#':
                index += 1
                return None
            else:
                root = TreeNode(values[index])
                index += 1
                # Build left child starting from index + 1
                root.left = build_tree(values)
                root.right = build_tree(values)
            return root
        return build_tree(data.split(" "))
