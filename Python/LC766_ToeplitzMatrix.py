class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] != matrix[i][j]:
                    return False
        return True
