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
    
    """
    Just remember the answer, no bullshit
    https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = sorted(Counter(tasks).values())[::-1]
        #print([str(a) for a in freq])
        max_freq = freq[0]
        max_count = 1
        i = 1
        while i < len(freq):
            if freq[i] == freq[i - 1]:
                max_count += 1
            else:
                break
            i += 1
        #print("{} {}".format(max_count, max_freq))
        parts = max_freq - 1
        slots_in_part = n - (max_count - 1)
        total_slots = parts * slots_in_part
        available_tasks = len(tasks) - max_count * max_freq
        return len(tasks) + max(0, total_slots - available_tasks)
