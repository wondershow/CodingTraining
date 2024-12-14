class Solution:
    """
    NlogK, heap solution
    """
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heap[0]
    
    """
    Quick select O(N)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find rank smallest val in nums
        """
        def helper(nums, lo, hi, rank):
            if rank == 1 and lo == hi:
                return nums[lo]
            rand_index = random.randint(lo, hi)
            nums[lo], nums[rand_index] = nums[rand_index], nums[lo]
            pivot = nums[lo]
            i, j, right = lo + 1, lo + 1, hi
            while i <= right:
                if nums[i] == pivot:
                    i += 1
                elif nums[i] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i, j = i + 1, j + 1
                else:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
            
            nums[right], nums[lo] = nums[lo], nums[right]
            if rank < j - lo + 1:
                return helper(nums, lo, j - 1, rank)
            if j - lo + 1 <= rank <= right - lo + 1:
                return nums[right]
            return helper(nums, i, hi, rank - (right - lo + 1))
        
        return helper(nums, 0, len(nums) - 1, len(nums) + 1 - k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        This method is much easier but it requires extra space. (Not in-pace)
        """
        def quick_select(array, k):
            small, equal, large = [], [], []
        pivot = random.choice(nums)
        for num in nums:
            if num < pivot:
                small.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                large.append(num)
        if k <= len(large):
            return self.findKthLargest(large, k)
        elif len(large) < k <= len(large) + len(equal):
            return pivot
        return self.findKthLargest(small, k - (len(large) + len(equal)))
