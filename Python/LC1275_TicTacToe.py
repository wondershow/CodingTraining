class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows, cols = [0] * 3, [0] * 3
        diagonal, anti_diagonal = 0, 0
        for i, move in enumerate(moves):
            row, col = move[0], move[1]
            delta = (-1)**(i%2)
            rows[row] += delta
            cols[col] += delta
            if row + col == 2:
                anti_diagonal += delta
            if row == col:
                diagonal += delta
            aux = [rows[row], cols[col], anti_diagonal, diagonal]
            if 3 in aux:
                return "A"
            if -3 in aux:
                return "B"
        return "Pending" if len(moves) < 9 else "Draw"
