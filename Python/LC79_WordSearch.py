class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtracking(x, y, suffix):
            if not suffix:
                return True
            if x < 0 or y < 0 or x == M or y == N or board[x][y] != suffix[0]:
                return False
            board[x][y] = '#'
            for dx, dy in deltas:
                x0, y0 = x + dx, y + dy
                if backtracking(x0, y0, suffix[1:]):
                    return True
            board[x][y] = suffix[0]
            return False
            

        M, N, deltas = len(board), len(board[0]), [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(M):
            for j in range(N):
                if backtracking(i, j, word):
                    return True
        return False
