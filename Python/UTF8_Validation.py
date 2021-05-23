class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        0XXXXXXX 0-127
        110XXXXX 192 - 223
        10XXXXXX 128 - 191
        1110XXXX 224 - 239
        11110XXX 240 - 247
        """
        i, N = 0, len(data)
        while i < N:
            if 0 <= data[i] < 128:
                i += 1
                continue
            if 192 <= data[i] < 224:
                delta = 1
            elif 224 <= data[i] < 240:
                delta = 2
            elif 240 <= data[i] < 248:
                delta = 3
            else:
                return False
            j = 1
            while j <= delta:
                if i + j >= N or data[i + j] < 128 or data[i + j] >= 192:
                    return False
                j += 1
            i = i + delta + 1
        return True
        
