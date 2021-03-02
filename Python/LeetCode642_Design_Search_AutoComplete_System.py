class TrieNode:
    def __init__(self):
        self.kids = defaultdict(TrieNode)
        self.prefix = []
    
    def add_prefix(self, sentence, time):
        for i, t in enumerate(self.prefix):
            if self.prefix[i][1] == sentence:
                self.prefix[i][0] = -time
                break
        else:
            self.prefix.append([-time, sentence])
        self.prefix.sort()
        if len(self.prefix) > 3:
            self.prefix.pop(-1)
            
    def find(self, c):
        if c not in self.kids:
            return (None, [])
        return (self.kids[c], [item[1]  for item in self.kids[c].prefix ] )

class AutocompleteSystem:
    
    def add_sentence_to_trie(self, root, sentence, time):
        node = root
        for c in sentence:
            node = node.kids[c]
            node.add_prefix(sentence, time)
        
        
    def __init__(self, sentences: List[str], times: List[int]):
        '''
        Use a trie to store all the sentences.
        Each node is stored with a letter, a space will also be stored, meanwhile '#' will be stored too. At each space, all same prefix sentences will be stored.
        when searching, for every single input, travel down from the root and return all the sentences with matched prefix       
        '''
        self.root = TrieNode()
        self.last_setence = ""
        self.cur_trie_node = self.root
        self.freq = {}
        
        for i, sentence in enumerate(sentences):
            self.freq[sentence] = times[i]
            self.add_sentence_to_trie(self.root, sentence, times[i])
        
    def input(self, c: str) -> List[str]:
        if c != '#':
            self.last_setence += c
            if not self.cur_trie_node:
                return []
            next_node, res = self.cur_trie_node.find(c)
            self.cur_trie_node = next_node
            return res
        else:
            self.freq[self.last_setence] = self.freq.get(self.last_setence, 0) + 1
            self.add_sentence_to_trie(self.root, self.last_setence, self.freq[self.last_setence])
            self.last_setence = ""
            self.cur_trie_node = self.root
            return []
