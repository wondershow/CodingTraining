class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M, N = len(matrix), len(matrix[0])
        self.aux = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                self.aux[i][j] = matrix[i - 1][j - 1] + self.aux[i - 1][j] + self.aux[i][j - 1] - self.aux[i - 1][j - 1]
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.aux[row2 + 1][col2 + 1] + self.aux[row1][col1] - self.aux[row2 + 1][col1] - self.aux[row1][col2 + 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
