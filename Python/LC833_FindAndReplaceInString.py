class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = ""
        tuples = [ (a, b, c) for a, b, c in zip(indices, sources, targets)]
        tuples.sort()
        i, N, j, M = 0, len(s), 0, len(tuples)
        while i < N:
            if j < M and tuples[j][0] == i:
                l = len(tuples[j][1])
                if s[i:i + l] == tuples[j][1]:
                    res += tuples[j][2]
                    i += l
                else:
                    res += s[i]
                    i += 1
                j += 1
            else:
                res += s[i]
                i += 1
        return res
            
            
            
            
        return res
                
    
