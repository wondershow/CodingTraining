class Solution:
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
                 
               
                
