class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        max_seen = float("-inf")
        for interval in intervals:
            if max_seen > interval[0]:
                return False
            max_seen = interval[1]
        return True
