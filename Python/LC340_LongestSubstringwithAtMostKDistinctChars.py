class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        N, count, j, res = len(s), {}, 0, 0
        for i in range(N):
            while j < N:
                # The break condition here is tricky
                # len(count) < k is not accurate, and has many edge caes 
                if len(count) == k and s[j] not in count:
                    break
                count[s[j]] = count.get(s[j], 0) + 1            
                j += 1
            res = max(res, j - i)
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
        #print(count)
        return res
