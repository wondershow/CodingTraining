class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        reverse_mapping = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i, word in enumerate(s.split()):
            if pattern[i] not in mapping and word not in reverse_mapping:
                mapping[pattern[i]] = word
                reverse_mapping[word] = pattern[i]
            elif pattern[i] not in mapping or word not in reverse_mapping:
                return False
            elif mapping[pattern[i]] != word:
                return False
        return True
