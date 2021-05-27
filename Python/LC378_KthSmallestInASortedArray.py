class Solution:
    """
    O(k*logk)
    """
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        heap = [[matrix[0][0], 0, 0]]
        R, C = len(matrix), len(matrix[0])
        seen = {(0, 0)}
        for _ in range(k - 1):
            _, x, y = heappop(heap)
            if x < R - 1 and (x + 1, y) not in seen:
                seen.add((x + 1, y))
                heappush(heap, [matrix[x + 1][y], x + 1, y])
            if y < C - 1 and (x, y + 1) not in seen:
                seen.add((x, y + 1))
                heappush(heap, [matrix[x][y + 1], x, y + 1])
        return heap[0][0]
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        heap = []
        for r in range(R):
            heappush(heap, [matrix[r][0], r, 0])
        for _ in range(k - 1):
            _, r, c = heappop(heap)
            if c + 1 < len(matrix[r]):
                heappush(heap, [matrix[r][c + 1], r, c + 1])
        return heap[0][0]
