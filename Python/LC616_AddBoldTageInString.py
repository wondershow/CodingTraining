class Solution:
    """
    1. find W of all words (max width)
    2. At each location of s, try to find substring from that location up to w in the word_dict, if yes, set it to 1
    3. Generate output
    
    Mistakes made:
    1. when getting substing, failed to consider the case when s[i:i+w] that i+w could be out of boundary
    2. Used append instead of "+" to concatenate strings
    """
    def addBoldTag1(self, s: str, word_dict: List[str]) -> str:
        if not s or not word_dict:
            return s
        N = len(s)
        W = max([len(word) for word in word_dict])
        word_dict = set(word_dict)
        bold = [0] * N
        for i, c in enumerate(s):
            for w in range(1, W + 1):
                if s[i: min(N, i + w)] in word_dict:
                    for j in range(i, min(N, i + w)):
                        bold[j] = 1
        res = ""
        for i, c in enumerate(s):
            if i == 0 and bold[i] == 1 or i > 0 and bold[i - 1] == 0 and bold[i] == 1:
                res += "<b>"
            res += c
            if i == N - 1 and bold[i] == 1 or i < N - 1 and bold[i + 1] == 0 and bold[i] == 1:
                res += "</b>"
        return res
    
    """
    Remember this method!
    """
    def addBoldTag(self, s: str, word_dict: List[str]) -> str:
        location = []
        N = len(s)
        if not s or not word_dict:
            return s
        bold = set()
        for word in word_dict:
            start = s.find(word)
            
            # Early termination
            while start != -1:
                for i in range(start, start + len(word)):
                    bold.add(i)
                start = s.find(word, start + 1)
        
        res = ""
        for i, c in enumerate(s):
            if i == 0 and i in bold or i > 0 and (i - 1) not in bold and i in bold:
                res += "<b>"
            res += c
            if i == N - 1 and i in bold or i < N - 1 and (i + 1) not in bold and i in bold:
                res += "</b>"
        return res
