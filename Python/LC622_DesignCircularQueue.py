class MyCircularQueue:

    """
    Add from rear, remove from head
    """
    def __init__(self, k: int):
        self.size, self.cap = 0, k
        self.head, self.tail = 0, 0
        self.arr = [0] * k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.tail] = value
        self.tail = (self.tail + 1) % self.cap
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.tail - 1) % self.cap]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
