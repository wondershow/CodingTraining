class Solution:
    """
    One method is count + heap
    O (NlogK)
    
    To do it o(N), we need to do quick select to find kth largest number
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        res = []
        for key, count in freq.items():
            heappush(heap, [count, key])
            if len(heap) > k:
                heappop(heap)
        return [b for a, b in heap]
