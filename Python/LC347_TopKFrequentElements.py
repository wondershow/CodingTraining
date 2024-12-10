class Solution:
    """
    One method is count + heap
    O (NlogK)
    
    To do it o(N), we need to do quick select to find kth largest number
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        heap = []
        for num, freq in counts.items():
            heappush(heap, (freq, num))
            if len(heap) > k:
                heappop(heap)
        return [b for a, b in heap]

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        topK = sorted(counts.items(), key=lambda item:item[1], reverse=True)[:k]
        return [a for a, b in topK]

    from collections import Counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        count = Counter(nums)
        
        # Sort by frequency (in descending order) but keep only the numbers
        return [num for num, _ in count.most_common(k)]

