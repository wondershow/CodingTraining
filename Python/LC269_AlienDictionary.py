class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph, alphabet = defaultdict(set), set()
        for word1, word2 in zip(words, words[1:]):
            alphabet.update(list(word1))
            for a, b in zip(word1, word2):
                if a != b:
                    graph[a].add(b)
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        alphabet.update(list(words[-1]))
        
        indegrees = defaultdict(int)
        for _, kids in graph.items():
            for kid in kids:
                indegrees[kid] += 1
                
        res, que = [], []
        for c in alphabet:
            if indegrees[c] == 0:
                que.append(c)
        
        
        while que:
            c = que.pop(0)
            res.append(c)
            for kid in graph[c]:
                indegrees[kid] -= 1
                if indegrees[kid] == 0:
                    que.append(kid)
        if len(res) != len(alphabet):
            return ""
        
        return "".join(res)
