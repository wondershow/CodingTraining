class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n - 1, 0, m - 1
        i = 0
        res = []
        while i < m * n:
            for col in range(left, right + 1):
                i += 1
                res.append(matrix[up][col])
            for row in range(up + 1, down + 1):
                i += 1
                res.append(matrix[row][right])
            if up < down:
                for col in range(right - 1, left - 1, -1):
                    i += 1
                    res.append(matrix[down][col])
            if left < right:
                for row in range(down - 1, up, -1):
                    i += 1
                    res.append(matrix[row][left])
            left, right, up, down = left + 1, right -1, up + 1, down - 1
        return res

