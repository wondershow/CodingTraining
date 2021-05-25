class Solution:
    """
    1. j starts from 1
    2. whenever does a write at j, move j to the next
    """
    def compress(self, chars: List[str]) -> int:
        count, j = 0, 1
        
        for i, c in enumerate(chars):
            if i > 0 and c != chars[i - 1]:
                if count > 1:
                    for n in str(count):
                        chars[j] = n
                        j += 1
                chars[j] = c
                j += 1
                count = 1
            else:
                count += 1
        
        if count > 1:
            for n in str(count):
                chars[j] = n
                j += 1
        return j
