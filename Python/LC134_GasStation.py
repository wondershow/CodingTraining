class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        total, min_subarray_sum_ending_index, min_subarray_sum = 0, 0, float("inf")
        for i in range(N):
            total += gas[i] - cost[i]
            if total < min_subarray_sum:
                min_subarray_sum_ending_index = i
                min_subarray_sum = total
        if total < 0:
            return -1
        return (min_subarray_sum_ending_index + 1) % N
