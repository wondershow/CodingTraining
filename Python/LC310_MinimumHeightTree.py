class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
          See the editorials here:https://leetcode.com/problems/minimum-height-trees/editorial/
          Idea: Keep removing leaf nodes of the tree until there are at most 2 left. 
        """
        if n <= 2:
            return [i for i in range(n)]
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        leaves = []
        for node, degree in adj_list.items():
            if len(degree) == 1:
                leaves.append(node)
        
        remaning = n 
        while remaning > 2:
            size = len(leaves)
            remaning -= size
            for _ in range(size):
                node = leaves.pop(0)
                for neigbhor in adj_list[node]:
                    adj_list[neigbhor].remove(node)
                    if len(adj_list[neigbhor]) == 1:
                        leaves.append(neigbhor)
        
        return leaves

            
