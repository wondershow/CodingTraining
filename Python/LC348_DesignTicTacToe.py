class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.cols, self.rows, self.diagonal, self.anti_diagonal = [0] * n, [0]* n, 0, 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        delta = 1 if player == 1 else -1
        
        self.cols[col] += delta
        self.rows[row] += delta
        
        if row + col == self.n - 1:
            self.anti_diagonal += delta
        if row == col:
            self.diagonal += delta
            
        if abs(self.cols[col]) == self.n or abs(self.rows[row]) == self.n or abs(self.anti_diagonal) == self.n or abs(self.diagonal) == self.n:
            return player
        return 0
