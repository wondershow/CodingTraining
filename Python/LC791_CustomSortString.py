class Solution:
    """
    Remember it!
    
    """
    def customSortString(self, order: str, str: str) -> str:
        #buckets = [i, v for i, v in enumerate(order)]
        freq = Counter(str)
        res = ""
        alphabet = set(list(order))
        for _, v in enumerate(order):
            if v in freq:
                res += v * freq[v]
        
        for c in str:
            if c not in alphabet:
                res += c
        return res
