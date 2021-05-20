class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq, heap = Counter(tasks), []
        for _, times in freq.items():
            heappush(heap, -times)
        
        cool_que, timer = [], 0
        while heap or cool_que:
            if heap:
                times = heappop(heap) + 1
                if times < 0:
                    cool_que.append([times, timer + n])
            
            if cool_que and cool_que[0][1] <= timer:
                heappush(heap, cool_que[0][0])
                cool_que.pop(0)
            
            timer += 1
        return timer
