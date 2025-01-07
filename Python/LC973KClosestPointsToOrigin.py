class Solution:
    """
    Sort and return version
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def comparator(p):
            return p[0] ** 2 + p[1] ** 2
        points.sort(key=comparator)
        return points[:k]
    
    """
    Carefully derive if we need a max heap or minheap, what to put as compare key in the heap
    Cautious!!
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            d = x * x + y * y
            heappush(max_heap, [-d, x, y])
            if len(max_heap) > k:
                heappop(max_heap)
        
        return [[x, y] for _, x, y in max_heap]
    
    
    """
    QuickSelect version
    """
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        aux = [(x ** 2 + y ** 2, x, y) for x , y in points]
    
        def quick_divde(aux, lo, hi, rank):
            if lo > hi:
                return
            pivot = aux[lo][0]
            cur, left, right = lo, lo, hi
            while cur <= right:
                if aux[cur][0] == pivot:
                    cur += 1
                elif aux[cur][0] > pivot:
                    aux[cur], aux[right] = aux[right], aux[cur]
                    right -= 1
                else:
                    aux[cur], aux[left] = aux[left], aux[cur]
                    left, cur = left + 1, cur + 1
            """
                When the while loop ends:
                < < < < < = = = = = = > > > > 
                          l         r c
                l => left, r => right, c=> cur
            """
            if left - lo + 1 <= rank <= cur - lo:
                return
            elif left - lo + 1 > rank:
                quick_divde(aux, lo, left - 1, rank)
            else:
                quick_divde(aux, cur, hi, rank - (cur - lo))

        quick_divde(aux, 0, len(aux) - 1, k)
        return [[x[1], x[2]] for x in aux[:k]]
