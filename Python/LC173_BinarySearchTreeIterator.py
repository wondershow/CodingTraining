# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack[-1].val
        p = self.stack.pop().right
        while p:
            self.stack.append(p)
            p = p.left
        return res

    def hasNext(self) -> bool:
        return bool(self.stack)
