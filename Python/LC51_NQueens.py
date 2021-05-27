class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generate_board(pos, n):
            res = []
            for i in range(n):
                line = ["."] * n
                line[pos[i]] = "Q"
                res.append("".join(line))
            return res
        
        cols, diagnoal, anti_diagnoal = set(), set(), set()
        def dfs(res, row, n, cur):
            nonlocal cols, diagnoal, anti_diagnoal
            if row == n:
                res.append(generate_board(cur, n))
                return
            for col in range(n):
                if col in cols or (row + col) in anti_diagnoal or (row - col) in diagnoal:
                    continue
                cols.add(col)
                anti_diagnoal.add(row + col)
                diagnoal.add(row - col)
                cur.append(col)
                dfs(res, row + 1, n, cur)
                cur.pop()
                cols.remove(col)
                anti_diagnoal.remove(row + col)
                diagnoal.remove(row - col)
        
        res = []
        dfs(res, 0, n, [])
        return res
