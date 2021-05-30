# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
The tricky part of this problem is "If two nodes are in the same row and column, the order should be from left to right." So it is not easy to tweak dfs to make i t right since with the same level (x, y).
Using BFS can gurantee the left, right order on same level.
The time complexity O(N)
"""
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        column_table = defaultdict(list)
        que, min_column, max_column = [(root, 0)], 0, 0
        while que:
            node, col = que.pop(0)
            column_table[col].append(node.val)
            min_column = min(min_column, col)
            max_column = max(max_column, col)
            if node.left:
                que.append((node.left, col - 1))
            if node.right:
                que.append((node.right, col + 1))
        
        
        res = []
        for col in range(min_column, max_column + 1):
            res.append(column_table[col])
        
        return res
