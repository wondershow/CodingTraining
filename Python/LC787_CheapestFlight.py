class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Dikjstra's method, heap.
        Need to use a minCostCity to remember cities have visited with a specific stop to do pruning
        """
        heap = []
        adj = defaultdict(list)
        for start, end, cost in flights:
            adj[start].append((end, cost))
        
        heap = [[0, src, k + 1]]
        minCostCity = {(src, 0): 0}
        while heap:
            cost, city, stops = heappop(heap)
            if city == dst:
                return cost
            for newCity, newCost in adj[city]:
                if stops > 0 and cost + newCost < minCostCity.get((newCity,stops - 1) , float("inf")):
                    minCostCity[(newCity,stops - 1) ] = cost + newCost
                    heappush(heap, (cost + newCost, newCity, stops - 1))
        return -1
