class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        aux = []
        for i, interval in enumerate(intervals):
            aux.append([interval[0], 1, i])
            aux.append([interval[1], 0, i])
        aux.sort()
        res, rooms = 0, 0
        for t in aux:
            if t[1] == 1:
                rooms += 1
            else:
                rooms -= 1
            res = max(res, rooms)
        return res
