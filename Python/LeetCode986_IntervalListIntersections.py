class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i, j, val, res = 0, 0, float("-inf"), []
        while i < len(firstList) and j < len(secondList):
            s1, e1, s2, e2 = firstList[i][0], firstList[i][1], secondList[j][0], secondList[j][1]
            if max(s1,s2) <= min(e1, e2):
                res.append([max(s1,s2), min(e1, e2)])
            if e1 <= e2:
                i += 1
            else:
                j += 1
        
        return res
