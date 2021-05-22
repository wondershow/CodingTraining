class Solution:
    """
    Mistakes made:
    1. outside the while loop, hits +1 not -1
    """
    def minWindow(self, s: str, t: str) -> str:
        counts, M, j = Counter(t), len(s), 0
        hits, N, min_len, res = 0, len(t), M + 1, ""
        for i in range(M):
            while j < M:
                if hits == N:
                    break
                counts[s[j]] -= 1
                if counts[s[j]] >= 0:
                    hits += 1
                j += 1
            if hits == N and j - i < min_len:
                min_len = j - i
                res = s[i:j]
            counts[s[i]] += 1
            if counts[s[i]] > 0:
                hits -= 1
        return res
