# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_biggest(node):
            while node.right:
                node = node.right
            return node.val
        
        def get_smallest(node):
            while node.left:
                node = node.left
            return node.val

        def delete(node, key):
            if not node:
                return node
            if key < node.val:
                node.left = delete(node.left, key)
            elif key > node.val:
                node.right = delete(node.right, key)
            else:
                if node.left:
                    biggest = get_biggest(node.left)
                    node.val = biggest
                    node.left = delete(node.left, biggest)
                elif node.right:
                    smallest = get_smallest(node.right)
                    node.val = smallest
                    node.right = delete(node.right, smallest)
                else:
                    node = None
            return node

        return delete(root, key)
                    



                
