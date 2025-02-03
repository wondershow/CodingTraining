"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(grid, x, y, size):
            if size == 1:
                return Node(True if grid[x][y] == 1 else False, True, None, None, None, None)
            topLeft = helper(grid, x, y, size // 2)
            topRight = helper(grid, x, y + size // 2, size // 2)
            bottomLeft = helper(grid, x + size // 2, y, size // 2)
            bottomRight = helper(grid, x + size // 2, y + size // 2,  size // 2)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None )
            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)
        return helper(grid, 0, 0, len(grid))
