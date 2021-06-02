class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] != matrix[i][j]:
                    return False
        return True
    
    """
    The solution to follow up one
    Note that in the inner loop, we have to loop from end to begining.
    """
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        M, N = len(matrix), len(matrix[0])
        seen = {}
        expected = matrix[0]
        for i in range(1, M):
            for j in range(N - 1, -1, -1):
                if j > 0 and matrix[i][j] != expected[j - 1]:
                    return False
                else:
                    expected[j] = matrix[i][j]
        return True
