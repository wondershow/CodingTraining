class Solution:
    """
    Greedy 
    https://www.youtube.com/watch?v=evesA3gr9BE
    """
    def shortestWay(self, source: str, target: str) -> int:
        t, N, ans = 0, len(source), 0
        while target:
            j = 0
            for i in range(N):
                if j < len(target) and source[i] == target[j]:
                    j += 1
            if j == 0:
                return - 1
            ans += 1
            target = target[j:]
            
        return ans
