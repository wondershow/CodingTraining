from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        index = self.events.bisect_right((start, end))
        if index > 0 and self.events[index - 1][1] > start or index < len(self.events) and self.events[index][0] < end:
            return False
        
        self.events.add((start, end))
        return True
