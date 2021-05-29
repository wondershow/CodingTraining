# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        stack1, stack2, p1, p2 = [], [], root1, root2
        while (p1 or stack1) or (p2 or stack2):
            while p1:
                stack1.append(p1)
                p1 = p1.left
            while p2:
                stack2.append(p2)
                p2 = p2.left
            if not stack1 and not stack2:
                break
            if not stack1 and stack2:
                res.append(stack2[-1].val)
                p2 = stack2.pop().right
                continue
            if stack1 and not stack2:
                res.append(stack1[-1].val)
                p1 = stack1.pop().right
                continue
                
            if stack1[-1].val < stack2[-1].val:
                res.append(stack1[-1].val)
                p1 = stack1.pop().right
            elif stack1[-1].val > stack2[-1].val:
                res.append(stack2[-1].val)
                p2 = stack2.pop().right
            else:
                res.append(stack1[-1].val)
                res.append(stack2[-1].val)
                p1 = stack1.pop().right
                p2 = stack2.pop().right
        return res
