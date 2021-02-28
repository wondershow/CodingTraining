class TrieNode:
    def __init__(self):
        self.kids = {}
        self.palinedrome_suffix = []
        self.flag = False
        self.index = -1
        self.word = ""

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        '''
            1. build a trie tree, forwarding order, meanwhile at each trie node, store the index(s) of word(s) which suffix is a palindrome.
            2. iterate the list of words, for each word, search it in the trie with its reverse order,
                2.1 when cur word ends and it reaches a trie node with true flag (this is a word) and that word is not the cur word, add pair to final result
                2.2 when cur word ends but trie ndoe is false flag but that trie node contains suffix palindromes add all pairs
                2.3 when cur word does not end but trie node reaches to bottom of the trie tree, AND the left part of cur word is a palindrome, add.
            3. watchout the "" case

        '''
        def build_trie_tree(words_list):
            root = TrieNode()
            for index, word in enumerate(words_list):
                node = root
                for i, c in enumerate(word):
                    if word[i:] == word[i:][::-1]:
                        node.palinedrome_suffix.append(index)
                    if c not in node.kids:
                        node.kids[c] = TrieNode()
                    node = node.kids[c]
                node.flag = True
                node.index = index
                node.word = word
            return root
        '''
        def debug_helper(root, trie_node, word, words):
            prefix, node = "", root
            for c in word:
                if c
                if c in node
                
            
            
            for i in trie_node.palinedrome_suffix:
                print("")'''

        res, trie_root = [], build_trie_tree(words)

        for index, word in enumerate(words):
            reversed_word = word[::-1]
            node = trie_root
            for i, c in enumerate(reversed_word):
                # reach bottom of a trie tree but our current node has not reached its end, case 2.3
                if node.flag and reversed_word[i:] == reversed_word[i:][::-1]:
                    res.append([node.index,  index])
                if c in node.kids:
                    node = node.kids[c]
                else:
                    break
            else: # We have reached end of "word" and it all matches
                #print("reacing end of word " + word)
                if node.flag and node.index != index: # case 2.1
                    res.append([node.index, index])
                for palindrome_index in node.palinedrome_suffix: # 2.2
                    res.append([palindrome_index, index])



        return res