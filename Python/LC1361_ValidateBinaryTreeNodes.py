class UF:
    def __init__(self, size):
        self.uf = [i for i in range(size)]
        
    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.uf[rx] = ry
    
    def get_total_components(self):
        seen = set()
        for i in range(len(self.uf)):
            seen.add(self.find(i))
        return len(seen)
        
        
class Solution:
    """
    UF.
    1. UF component size = 1
    edges = n - 1
    all indegrees = 1
    """
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = UF(n)
        indegrees, edges = {}, 0
        for i in range(n):
            if leftChild[i] != -1:
                uf.union(leftChild[i], i)
                indegrees[leftChild[i]] = indegrees.get(leftChild[i], 0) + 1
                edges += 1
            if rightChild[i] != -1:
                uf.union(rightChild[i], i)
                indegrees[rightChild[i]] = indegrees.get(rightChild[i], 0) + 1
                edges += 1
        return edges == n - 1 and uf.get_total_components() == 1 and all([a == 1 for a in indegrees.values()])
    
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        """
        1. n - 1 edges
        2. only 1 vertex has zero indegree
        3. all others has 1 indegree
        4. use topo sort to check if there is only one component
        """
        
        edges = 0
        indegrees = {}
        for parent, kids in enumerate(zip(leftChild, rightChild)):
            if kids[0] != -1:
                edges += 1
                indegrees[kids[0]] = indegrees.get(kids[0], 0) + 1
            if kids[1] != -1:
                edges += 1
                indegrees[kids[1]] = indegrees.get(kids[1], 0) + 1
        if edges != n - 1 or len(indegrees) != n - 1:
            print("aaa")
            return False
        
        que = []
        for i in range(n):
            if i not in indegrees:
                que.append(i)
            elif indegrees[i] != 1:
                print("bbb")
                return False
        
        #print(str(len(que)))
        seen = set(que)
        while que:
            node = que.pop(0)
            if leftChild[node] != -1:
                seen.add(leftChild[node])
                que.append(leftChild[node])
            if rightChild[node] != -1:
                seen.add(rightChild[node])
                que.append(rightChild[node])
        #print(str(len(seen)))
        return len(seen) == n
