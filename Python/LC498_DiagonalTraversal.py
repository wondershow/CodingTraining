class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        The idea is to let a cursor to travel from up to down of first column, 
        then travel from left to right last row.
        """
        M, N = len(mat), len(mat[0])
        res = []
        for x in range(M + N - 1):
            tmp = []
            i = min(M - 1, x)
            j = max(x - i, 0)
            while 0 <= i < M and 0 <= j < N:
                tmp.append(mat[i][j])
                i, j = i - 1, j + 1
            if x % 2 == 1:
                tmp.reverse()
            res.extend(tmp)
        return res
