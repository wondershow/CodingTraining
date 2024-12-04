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


    """
    For this method, we pass in a customized key.
    """
    def customSortString1(self, order: str, s: str) -> str:
        arr = sorted(list(s), key=lambda x: order.index(x) if x in order else 100)
        return "".join(arr)
