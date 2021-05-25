class Solution:
    """
    Just use basic rules
    1. when X = O, the next player is X, so O can not win
    2. when X > O, the next player is O, so X can not win
    3. X, O can not win at the same time
    4. 0 <= |X - O| <= 1
    """
    def validTicTacToe(self, board: List[str]) -> bool:
        def can_win(board, letter):
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] == letter:
                    return True
                if board[0][i] == board[1][i] == board[2][i] == letter:
                    return True
            if board[0][0] == board[1][1] == board[2][2] == letter:
                return True
            if board[2][0] == board[1][1] == board[0][2] == letter:
                return True
            return False
        
        x, o = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    x += 1
                elif board[i][j] == "O":
                    o += 1
        if x - o < 0 or x - o > 1:
            return False
        
        if can_win(board, 'O') and x > o:
            return False
        
        if can_win(board, 'X') and x == o:
            return False
        
        return True
