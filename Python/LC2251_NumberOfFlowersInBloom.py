class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = [], []
        for start, end in flowers:
            starts.append(start)
            ends.append(end)
        starts.sort()
        ends.sort()
        res = []

        for arrival in people:
            started = bisect_right(starts, arrival)
            ended = bisect_left(ends, arrival)
            res.append(started - ended)
        return res

