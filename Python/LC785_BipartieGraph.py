class Solution:
    """
        User a coloring algorithm to color each node (only 2 color), with BFS (use for loop in case there are multiple components)
        
        Then after coloring, compare each edge's two vertex, if they belong to same color, return fale
        
        Mistakes made:
        1. Failed to add new node to que in bfs
        2. At the comparing stage used '!=' instead of "="
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, color, seen = len(graph), {}, set()
        for i in range(n):
            if i not in seen:
                seen.add(i)
                color[i] = 0
                que = [i]
                while que:
                    node = que.pop(0)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            color[nei] = (color[node] + 1) % 2
                            que.append(nei)
        
        for i in range(n):
            for nei in graph[i]:
                
                # It is '==' here not '!='
                if color[i] == color[nei]:
                    return False
        return True
