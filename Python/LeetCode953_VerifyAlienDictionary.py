class Solution:
    """
    Road map: for letters in 'order', use its index as precedence indicator and built a map
    for word - to - word comparison if we found a pair of precedence, verify its order in the map (a -> b and a's index
    is smaller than b's index)
    """
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {a : i for i, a in enumerate(order)}
        
        for word1, word2 in zip(words, words[1:]):
            #print("{} {}".format(word1, word2))
            for a, b in zip(word1, word2):
                if a != b:
                    if order_map[a] >= order_map[b]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        
        return True
