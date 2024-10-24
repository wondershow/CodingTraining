class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def equals(counts1: dict, counts2: dict):
            for key, val in counts1.items():
                if val != counts2.get(key, 0):
                    return False
            return True

        if len(s1) > len(s2):
            return False
        counts1 = Counter(s1)
        counts2 = Counter(s2[:len(s1)])
        for i in range(len(s1) - 1, len(s2)):
            if i >= len(s1):
                counts2[s2[i]] += 1
                counts2[s2[i - len(s1)]] -= 1
            if equals(counts1, counts2):
                return True
        return False

