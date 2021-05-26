class Solution:
    """
    Just remember this
    """
    def minAreaRect(self, points: List[List[int]]) -> int:
        lines = defaultdict(set)
        for x, y in points:
            lines[x].add(y)
        
        min_area, N = float("inf"), len(points)
        for i in range(N):
            x0, y0 = points[i]
            for j in range(i + 1, N):
                x1, y1 = points[j]
                if x0 == x1 or y0 == y1:
                    continue
                area = abs(x0 - x1) * abs(y0 - y1)
                if area > min_area:
                    continue
                if y1 in lines[x0] and y0 in lines[x1]:
                    min_area = area
        return 0 if min_area == float("inf") else min_area
