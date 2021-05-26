class Solution:
    
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(int)
        for i, num in enumerate(nums):
            if freq[num] > 0:
                return True
            freq[num] = freq[num] + 1
            if i >= k:
                freq[nums[i - k]] -= 1
        return False
    
    """
    This is much easier to do
    """
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i, num in enumerate(nums):
            if num in freq and i - freq[num] <= k:
                return True
            freq[num] = i
        return False
