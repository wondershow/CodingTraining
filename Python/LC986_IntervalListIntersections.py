class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res, i, j = [], 0, 0
        while i < len(firstList) and j < len(secondList):
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                j += 1
            else:
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                elif firstList[i][1] > secondList[j][1]:
                    j += 1
                else:
                    i, j = i + 1, j + 1
        return res

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Seems to be more concise
        """
        i, j, M, N = 0, 0, len(firstList), len(secondList)
        res = []
        while i < M and j < N:
            a, b = firstList[i], secondList[j]
            if a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]:
                res.append([max(a[0], b[0]), min(a[1], b[1])])
            if a[1] < b[1]:
                i += 1
            else:
                j += 1
        return res

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res, l1, l2 = [], 0, 0
        while l1 < len(firstList) and l2 < len(secondList):
            start = max(firstList[l1][0], secondList[l2][0])
            end = min(firstList[l1][1], secondList[l2][1])
            if start <= end:
                res.append([start, end])
            if firstList[l1][1] < secondList[l2][1]:
                l1 += 1
            else:
                l2 += 1
        return res
