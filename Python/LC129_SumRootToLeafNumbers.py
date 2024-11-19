class Solution:
    """
    This version is 2021
    """
    def findMaxLength(self, nums: List[int]) -> int:
        seen, running, res = {0: -1}, 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                running += 1
            else:
                running -= 1
            if running in seen:
                res = max(res, i - seen[running])
            else:
                seen[running] = i
        return res

    """
    This version is 2024 Nov
    """
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def preOrder(node, val):
            nonlocal res
            val = 10 * val + node.val
            if not node.left and not node.right:
                res += val
            if node.left:
                preOrder(node.left, val)
            if node.right:
                preOrder(node.right, val)
        preOrder(root, 0)
        return res
