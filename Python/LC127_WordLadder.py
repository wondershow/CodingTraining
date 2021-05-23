class Solution:
    """
    Time: O(N*26*W^2)
    Space complexity is O(N*W)
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que, seen = [(beginWord, 1)], {beginWord}
        word_set = set(wordList)
        alphabet = set(list("abcdefghijklmnopqrstuvwxyz"))
        while que:
            word, depth = que.pop(0)
            if word == endWord:
                return depth
            for i in range(len(word)):
                chars = list(word)
                for c in alphabet:
                    chars[i] = c
                    neighbor = "".join(chars)
                    if neighbor in seen or neighbor not in word_set:
                        continue
                    seen.add(neighbor)
                    que.append((neighbor, depth + 1))
        return 0
            
