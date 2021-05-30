class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        1. build graph
        2. build indegrees
        3. do topo sort
        this version is consise. build graph, indegrees, alphabet in 1 pass
        then do toposort, check valid in 2 places. 
        """
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        alphabet = set()
        for word1, word2 in zip(words, words[1:]):
            alphabet.update(list(word1))
            for a, b in zip(word1, word2):
                if a != b:
                    graph[a].append(b)
                    indegrees[b] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        alphabet.update(list(words[-1]))
        que = [c for c in alphabet if indegrees[c] == 0]
        topo_order = []
        while que:
            node = que.pop(0)
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    que.append(neighbor)
        if len(topo_order) == len(alphabet):
            return "".join(topo_order)
        return "" 
