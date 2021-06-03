class MedianFinder:
    """
    Mistakes made:
    Failed to check if min_heap is empty when trying to get its heap top
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap, self.min_heap = [], []

    def balance(self):
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
        
    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        self.balance()

    def findMedian(self) -> float:
        if (len(self.max_heap) + len(self.min_heap)) % 2 == 1:
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
