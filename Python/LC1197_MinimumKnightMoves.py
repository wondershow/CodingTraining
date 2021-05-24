class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[1, 2], [2, 1], [1, -2], [-2, 1], [-1, 2], [2, -1], [-1, -2], [-2, -1]]
        seen = {(0, 0)}
        que = [(0, 0, 0)]
        x, y = abs(x), abs(y)
        while que:
            i, j, step = que.pop(0)
            if x == i and y == j:
                return step
            for di, dj in directions:
                i0, j0 = i + di, j + dj
                if (i0, j0) not in seen and i0 >= -2 and j0 >= -2:
                    seen.add((i0, j0))
                    que.append((i0, j0, step + 1))
        return 0
