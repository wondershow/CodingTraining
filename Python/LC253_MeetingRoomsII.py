class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        aux = []
        for start, end in intervals:
            aux.append([start, 1])
            aux.append([end, -1])
        aux.sort()
        rooms = 0
        for _, delta in aux:
            rooms += delta
            res = max(res, rooms)
        return res
