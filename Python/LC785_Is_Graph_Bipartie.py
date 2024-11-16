class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen, que = {}, [0]

        for i in range(len(graph)):
            if i in seen:
                continue
            seen[i], que = 0, [i]
            while que:
                node = que.pop(0)
                for neighbor in graph[node]:
                    if neighbor in seen and seen[neighbor] == seen[node]:
                        return False
                    elif neighbor not in seen:
                        seen[neighbor] = seen[node] ^ 1
                        que.append(neighbor)
        return True
