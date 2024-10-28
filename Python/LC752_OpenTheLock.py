class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends, seen = set(deadends), set()
        queue = [((0, 0, 0, 0), 0)]
        seen.add((0, 0, 0, 0))
        deltas = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 1, 0], [0, 0, -1, 0], [0, 1, 0, 0], [0, -1, 0, 0], [1, 0, 0, 0], [-1, 0, 0, 0]]
        while queue:
            combo, steps = queue.pop(0)
            string = (str(combo[0]) + str(combo[1]) + str(combo[2]) + str(combo[3]))
            if string == target:
                return steps
            for d0, d1, d2, d3 in deltas:
                x0, x1, x2, x3 = (combo[0] + d0) % 10, (combo[1] + d1) % 10, (combo[2] + d2) % 10, (combo[3] + d3) % 10
                if (x0, x1, x2, x3) not in seen and string not in deadends:
                    queue.append([(x0, x1, x2, x3), steps + 1])
                    seen.add((x0, x1, x2, x3))
        return -1
