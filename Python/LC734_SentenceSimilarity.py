class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similar_dict = defaultdict(set)
        for word1, word2 in similarPairs:
            similar_dict[word1].add(word2)
            similar_dict[word2].add(word1)
        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue
            if word1 not in similar_dict or word2 not in similar_dict[word1]:
                return False
        return True
