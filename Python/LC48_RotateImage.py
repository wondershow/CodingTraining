class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(matrix):
            N = len(matrix)
            for i in range(N):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reflectRows(matrix):
            N = len(matrix)
            for i in range(N):
                for j in range(N // 2):
                    matrix[i][j], matrix[i][N - 1 - j] = matrix[i][N - 1 - j], matrix[i][j]

        transpose(matrix)
        reflectRows(matrix)

    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
