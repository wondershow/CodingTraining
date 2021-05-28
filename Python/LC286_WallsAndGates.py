class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def get_gates(rooms):
            res = []
            M, N = len(rooms), len(rooms[0])
            for i in range(M):
                for j in range(N):
                    if rooms[i][j] == 0:
                        res.append((i, j))
            return res
        
        que = [(i, j, 0) for i, j in get_gates(rooms)]
        #seen = set()
        deltas = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        R, C = len(rooms), len(rooms[0])
        INF = 2**31 - 1
        while que:
            i, j, distance = que.pop(0)
            for dx, dy in deltas:
                x, y = i + dx, j + dy
                if 0 <= x < R and 0 <= y < C and rooms[x][y] == INF:
                    rooms[x][y] = distance + 1
                    que.append((x, y, distance + 1))
