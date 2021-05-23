class Solution:
    """
    Count the top left corner of a ship.
    Condition to determin a top left corner of a ship:
    1. its left is dot, if it has one, its top is a dop if it has one

    """
    def countBattleships(self, board: List[List[str]]) -> int:
        M, N = len(board), len(board[0])
        res = 0
        for i in range(M):
            for j in range(N):
                if board[i][j] == ".":
                    continue
                if i > 0 and board[i - 1][j] == "X":
                    continue
                if j > 0 and board[i][j - 1] == "X":
                    continue
                res += 1
        return res
