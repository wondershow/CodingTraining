class Solution:
    """
    Memoization dfs.
    Mistakes made:
    1. When initing the jump hash, failed to add 5 as an empty list.
    2. When initing the memo hash, failed to set up the key as a tuple but set it as just the index
    
    Could be optimized by symmetric
    """
    def knightDialer1(self, n: int) -> int:
        jump = {1 : [6, 8], 2: [7, 9], 3:[4,8], 4: [3, 9, 0], 5:[],  6: [1, 7, 0], 7: [2, 6], 8:[1,3], 9:[2, 4], 0:[4, 6] }
        mod = 10**9 + 7
        memo = { (i, 1) : 1 for i in range(10)}
        
        def dfs(num, n, memo, jump, mod):
            if (num, n) in memo:
                return memo[(num, n)]
            res = 0
            for i in jump[num]:
                res += dfs(i, n - 1, memo, jump, mod)
            res = res % mod
            memo[(num, n)] = res
            return res
        
        res = 0
        for i in range(10):
            res += dfs(i, n, memo, jump, mod)
        
        return res % mod
    
    
    """
    DP
    """
    def knightDialer(self, n: int) -> int:
        jump = {1 : [6, 8], 2: [7, 9], 3:[4,8], 4: [3, 9, 0], 5:[],  6: [1, 7, 0], 7: [2, 6], 8:[1,3], 9:[2, 4], 0:[4, 6] }
        
        
        cur_count = [1] * 10
        
        for _ in range(n - 1):
            next_count = [0] * 10
            for i in range(10):
                for from_number in jump[i]:
                    next_count[i] = (next_count[i] + cur_count[from_number]) % (10**9 + 7)
            cur_count = next_count
        return sum(cur_count) % (10**9 + 7)
