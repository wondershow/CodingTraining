class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        time = {a + 1:time[a] for a in range(n)}

        answer = {}
        adj = defaultdict(list)
        indegree = defaultdict(int)
        maxPrev = defaultdict(int)

        for prevCoursej, nextCoursej in relations:
            adj[prevCoursej].append(nextCoursej)
            indegree[nextCoursej] += 1
        
        que = [a for a in range(1, n + 1) if indegree[a] == 0]
        answer = { a : time[a] for a in que}
        while que:
            nextCourse = que.pop(0)
            for adv in adj[nextCourse]:
                maxPrev[adv] = max(maxPrev[adv], answer[nextCourse])
                indegree[adv] -= 1
                if indegree[adv] == 0:
                    answer[adv] = time[adv] + maxPrev[adv]
                    que.append(adv)
        return max(answer.values())
        
