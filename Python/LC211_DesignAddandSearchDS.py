class Trie:
    def __init__(self):
        self.kids = {}
        self.is_word = False

"""
O(N) N is the length of the input word when N does not have "."
Worse case scenario, O(26^N)
"""
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.kids:
                node.kids[c] = Trie()
            node = node.kids[c]
        node.is_word = True
    
    def search_helper(self, word, index, node):
        if index == len(word):
            return node.is_word
        c = word[index]
        if c != ".":
            if c not in node.kids:
                return False
            return self.search_helper(word, index + 1, node.kids[c])
        else:
            """
            Made a mistake in the follwing like of code. We need to iterate
            all the dictionary values, not keys
            """
            for kid in node.kids.values():
                if self.search_helper(word, index + 1, kid):
                    return True
            return False

    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
