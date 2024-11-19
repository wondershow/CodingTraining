class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image

        que, seen = [(sr, sc)], set([(sr, sc)])
        image[sr][sc] = color
        deltas = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while que:
            x, y = que.pop()
            for dx, dy in deltas:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < M and 0 <= y1 < N and (x1, y1) not in seen and image[x1][y1] == original_color:
                    image[x1][y1] = color
                    seen.add((x1, y1))
                    que.append((x1, y1))
        return image
