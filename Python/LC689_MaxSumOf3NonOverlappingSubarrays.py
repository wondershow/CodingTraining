class Solution:
    """
        This is a very tedious question.
        
        We need to build 2 arrays:
        left[i] is the starting index of max_sum subarray of size k in 0...i - 1
        right[i] is the starting index of max_sum subarray of size k in i....N - 1
        
        then we iterate from k to n - k
        find the max value
        O(N)
    """
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        """
        left[i] is the starting index of max_sum subarray of size k in 0...i - 1
        right[i] is the starting index of max_sum subarray of size k in i....N - 1
        """
        left, right = [-1] * N, [-1] * N
        
        max_seen_left = sum(nums[:k])
        
        left[k - 1], running_sum_left = 0, max_seen_left
        left_max_sum = {k - 1: max_seen_left}
        for i in range(k, N):
            running_sum_left += nums[i] - nums[i - k]
            left[i] = left[i - 1]
            left_max_sum[i] = left_max_sum[i - 1]
            if running_sum_left > max_seen_left:
                max_seen_left = running_sum_left
                left[i] = i - k + 1
                left_max_sum[i] = max_seen_left
        
        max_seen_right = sum(nums[-k:])
        right_max_sum = {N - k: max_seen_right}
        right[N - k], running_sum_right = N - k, max_seen_right
        for i in range(N - k - 1, -1, -1):
            running_sum_right += nums[i] - nums[i + k]
            right[i] = right[i + 1]
            right_max_sum[i] = right_max_sum[i + 1]
            if running_sum_right >= max_seen_right:
                max_seen_right = running_sum_right
                right[i] = i
                right_max_sum[i] = max_seen_right
        #for i, start_index in enumerate(right):
            #print("after {} max {} which starts at {}".format(i, right_max_sum.get(i, 0), start_index))
        
        max_val = float("-inf")
        res = []
        for i in range(k, N - 2 * k + 1):
            local_max = left_max_sum[i - 1] + (prefix_sum[i + k] - prefix_sum[i]) + right_max_sum[i + k]
            if local_max > max_val:
                max_val = local_max
                #print("{} {} {}".format(left_max_sum[i - 1], (prefix_sum[i + k] - prefix_sum[i]), right_max_sum[i + k]))
                
                # Mistakes make here,  right[i + k] not  right[i + 1] !!!!left[i - 1] not left[i]
                res = [left[i - 1], i, right[i + k]]
                
        print(str(max_val))
        return res
        
        
        
        
        
