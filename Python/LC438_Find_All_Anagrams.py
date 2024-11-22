class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N, freq = len(p), Counter(p)
        right, hits, res = 0, 0, []

        # Watch out for the range condition
        for i in range(len(s) - N + 1):
            while right < i + N:
                if freq.get(s[right], 0) > 0: 
                    hits += 1
                freq[s[right]] = freq.get(s[right], 0) - 1
                right += 1
            if hits == N:
                res.append(i)
            if freq[s[i]] >= 0:
                hits -= 1
            freq[s[i]] += 1
        return res

