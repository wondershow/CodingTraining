class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        heaps = defaultdict(list)
        for id, score in items:
            heappush(heaps[id], score)
            if len(heaps[id]) > 5:
                heappop(heaps[id])
        #print(heaps)
        res = [[id, sum(top_scores) // len(top_scores)] for id, top_scores in heaps.items()]
        res.sort(key=lambda x: (x[0]))
        return res
