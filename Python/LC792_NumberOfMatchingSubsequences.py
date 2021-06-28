class Solution:
    """
    Speechless, see https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
    """
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        bucket = defaultdict(list)
        for word in words:
            bucket[word[0]].append((word, 1))
        ans = 0
        for c in s:
            if c in bucket and len(bucket[c]) > 0:
                N = len(bucket[c])
                for _ in range(N):
                    word, index = bucket[c].pop(0)
                    if index == len(word):
                        ans += 1
                    else:
                        bucket[word[index]].append((word, index + 1))
        return ans
