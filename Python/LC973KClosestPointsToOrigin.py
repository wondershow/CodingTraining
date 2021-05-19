class Solution:
    """
    Carefully derive if we need a max heap or minheap, what to put as compare key in the heap
    Cautious!!
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            d = x * x + y * y
            heappush(max_heap, [-d, x, y])
            if len(max_heap) > k:
                heappop(max_heap)
        
        return [[x, y] for _, x, y in max_heap]
