class UnionFind:
    def __init__(self, size):
        self.uf = [i for i in range(size)]
        self.components = size
    
    # a is 0-based index
    def root(self, a):
        if self.uf[a] != a:
            self.uf[a] = self.root(self.uf[a])
        return self.uf[a]

    def union(self, a, b):
        r1, r2 = self.root(a), self.root(b)
        if r1 != r2:
            self.uf[r1] = r2
            self.components -= 1
        
    def size(self):
        return self.components

class Solution:
    def validTree1(self, n: int, edges: List[List[int]]) -> bool:
        """
        Detect if 
        1. there are n - 1 edges
        2. All the nodes are in 1 connected component

        For 2, we can either use a trivial dfs/bfs or a union find
        """
        if len(edges) != n - 1:
            return False
        queue, seen = [[0, -1]], set([0])
        sources = defaultdict(list)
        for src, dst in edges:
            sources[src].append(dst)
            sources[dst].append(src)

        while queue:
            node, source = queue.pop(0)
            for neighbor in sources[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append([neighbor, node])
        return len(seen) == n == len(edges) + 1

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        return uf.size() == 1 and len(edges) == n - 1
