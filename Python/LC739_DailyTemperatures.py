class Solution:
    """
    Use a monotonic stack to keep all increasing temps indexes.
    Iterate from last to first
    
    REMEMBER to reverse the res
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, N, res = [], len(temperatures), []
        for i in range(N - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                res.append(stack[-1] - i)
            else:
                res.append(0)
            stack.append(i)
        return res[::-1]
        
