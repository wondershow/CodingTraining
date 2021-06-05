class MaxStack:
    """
    This problem is tricky, just remember the answer:
    1. User a decreasing sequence to attach to each push.
    2. stack to track all elements, max_heap to keep track of the max value
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.heap = []
        self.seq = 0
        self.deleted = set()
        

    def push(self, x: int) -> None:
        self.stack.append((x, self.seq))
        heappush(self.heap, (-x, self.seq))
        self.seq -= 1

    def pop(self) -> int:
        x, seq = self.stack.pop()
        self.deleted.add(seq)
        self._move()
        return x
        
    def _move(self):
        while self.heap and self.heap[0][1] in self.deleted:
            heappop(self.heap)
        while self.stack and self.stack[-1][1] in self.deleted:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return -self.heap[0][0]

    def popMax(self) -> int:
        res, seq = heappop(self.heap)
        self.deleted.add(seq)
        self._move()
        return -res


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
