class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.arr = [0] * k
        self.size = 0
        self.cap = k
        self.front = 0
        self.tail = k - 1 
        
        """Front adds from right side"""
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.front] = value
        self.size += 1
        self.front = (self.front + 1) % self.cap
        return True
        
        
        """Tail adds from left side"""
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.arr[self.tail] = value
        self.size += 1
        self.tail = (self.tail - 1 + self.cap) % self.cap
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front - 1 + self.cap) % self.cap
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.tail = (self.tail + 1) % self.cap
        self.size -= 1
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.front - 1 + self.cap) % self.cap]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        return self.arr[(self.tail + 1) % self.cap]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.cap


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
