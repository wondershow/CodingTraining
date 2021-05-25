class Solution:
    """
    This is a pretty expensive solution, theoretically o(NK)
    """
    def medianSlidingWindow1(self, nums: List[int], k: int) -> List[float]:
        window, medians = sorted(nums[:k]), []
        for a, b in zip(nums, nums[k:] + [2]):
            medians.append((window[(k)//2] + window[(k - 1)//2]) / 2)
            window.remove(a)
            bisect.insort(window, b)
        return medians
    
    
    """
    Lazy Deletion and maintain two balanced-size heaps  on the go
    
    push [value, index] to min_heap, or max_heap
    
    at initialization phase, the len(min_heap) = len(max_heap) (or + 1)
    
    at each iteration, we need to know when it is "inbalanced", adding new value to one heap while deleting from another, this case, we need to re-balance
    
    see the code interpretation.
    Mistakes made:
    1. Failed to do get_median before the main loop
    2. Used "if nums[i - k] < min_heap[0][0]:" as condition to balance heaps (see comments)
    """
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        min_heap, max_heap = [], []
        for i, v in enumerate(nums[:k]):
            heappush(min_heap, [v, i])
        
        for i in range(k // 2):
            v, index = heappop(min_heap)
            heappush(max_heap, [-v, index])
        
        def get_median(min_heap, max_heap, k):
            if k % 2 == 0:
                return (min_heap[0][0] - max_heap[0][0]) / 2
            return min_heap[0][0]/1.0
        
        def move(heap1, heap2):
            v, i = heappop(heap1)
            heappush(heap2, [-v, i])
        
        ans = [get_median(min_heap, max_heap, k)]
        for i in range(k, len(nums)):
            v = nums[i]
            #print("kicking {} {} adding {} {}".format(i - k, nums[i - k], i, nums[i]))
            if v >= min_heap[0][0]:
                heappush(min_heap,  [v, i])
                
                # Adding to min_heap, while deleting in max_heap, we need to call 'move' to 
                # do one-step re-balancing
                """
                if nums[i - k] < min_heap[0][0]:
                ^^^^ This statement is not working here. Since in one edge case, when all elements
                are equal, using this condition will only add elements to min_heap, the heaps will not
                be balanced.
                """
                if max_heap and nums[i - k] <=  -max_heap[0][0]:
                    move(min_heap, max_heap)
            else:
                
                # Adding to max_heap, while deleting in min_heap, we need to call 'move' to 
                # do one-step re-balancing
                heappush(max_heap,  [-v, i])
                if min_heap and nums[i - k] >=  min_heap[0][0]:
                    move(max_heap, min_heap)
                """
                ^^^ It should be noted that the above two 'move' calls wont move outdated entries, since we used two 'while' loops to evict
                outdated entries at the top of each heap until heap top is a valid entry (in the current window).
                """
            while min_heap and min_heap[0][1] + k <= i:
                heappop(min_heap)
            while max_heap and max_heap[0][1] + k <= i:
                heappop(max_heap)
            ans.append(get_median(min_heap, max_heap, k))
        return ans        
