class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        cur = k = i = 0
        while 3 + len(str(k)) * 2 < limit and cur + len(message) + (3 + len(str(k))) * k > k * limit:
            k += 1
            cur += len(str(k))
        
        res = []
        if 3 + len(str(k)) * 2 < limit:
            for j in range(1, k + 1):
                l = limit - 3 - len(str(k)) - len(str(j))
                res.append(f'{message[i:i + l]}<{j}/{k}>')
                i += l
        return res
