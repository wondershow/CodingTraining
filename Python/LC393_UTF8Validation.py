class Solution:
    """
    Just be careful
    """
    def validUtf8(self, data: List[int]) -> bool:
        if not data:
            return True
        i, N = 0, len(data)
        while i < N:
            delta = 0
            if 0 <= data[i] <= 127:
                delta = 0
            elif 192 <= data[i] <= 223:
                delta = 1
            elif 224 <= data[i] <= 239:
                delta = 2
            elif 240 <= data[i] <= 247:
                delta = 3
            else:
                return False
            i += 1
            if i + delta > N:
                return False
            while delta > 0:
                if data[i] < 128 or data[i] >= 192:
                    return False
                delta, i = delta - 1, i + 1
        return True
