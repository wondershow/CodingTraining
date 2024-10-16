class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in list(word):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word

    def search(self, word: str) -> bool:
        node = self.root
        for c in list(word):
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word != ""


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in list(prefix):
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
