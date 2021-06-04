class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        min_diagonal, max_diagnoal = float("inf"), float("-inf")
        for x, row in enumerate(nums):
            for y, num in enumerate(row):
                min_diagonal = min(min_diagonal, x + y)
                max_diagnoal = max(max_diagnoal, x + y)
                diagonals[x + y].append(num)
        res = []
        for i in range(min_diagonal, max_diagnoal + 1):
            
            """
            diagonals[i].reverse() !!!
            """
            diagonals[i].reverse()
            res.extend(diagonals[i])
        return res
