class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = {}
        for adv, base in prerequisites:
            graph[base].append(adv)
            indegrees[adv] = indegrees.get(adv, 0) + 1
        
        que = [ i for i in range(numCourses) if i not in indegrees]
        
        order = []
        while que:
            base = que.pop(0)
            order.append(base)
            for adv in graph[base]:
                indegrees[adv] -= 1
                if indegrees[adv] == 0:
                    que.append(adv)
        
        return len(order) == numCourses
        
        
