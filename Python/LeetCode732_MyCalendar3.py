class MyCalendarThree:

    def __init__(self):
        self.events = {}

    def book(self, start: int, end: int) -> int:
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1
        res, count = 0, 0
        for x in sorted(self.events):
            count += self.events[x]
            res = max(res, count)
        return res
