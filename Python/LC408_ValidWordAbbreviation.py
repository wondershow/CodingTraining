class Solution:
    """
    Missed one edge case which is when 
    the number part starts with 0
    like a04
    """
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        M, N = len(word), len(abbr)
        while i < M and j < N:
            if abbr[j].isdigit():
                val = 0
                
                
                if abbr[j] == '0':
                    return False
                while j < N and abbr[j].isdigit():
                    val = val * 10 + int(abbr[j])
                    j += 1
                i = i + val
            else:
                if word[i] != abbr[j]:
                    return False
                i, j = i + 1, j + 1
        return i == M and j == N
