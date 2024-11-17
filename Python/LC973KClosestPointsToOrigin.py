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
        aux = [[x*x + y*y, x, y] for x, y in points]
        def kth(aux, lo, hi, k):
            if lo >= hi:
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
                    cur, left = cur + 1, left + 1
            if left - lo + 1 <= k <= right - lo + 1:
                return
            elif k < left - lo + 1:
                kth(aux, lo, left - 1, k)
            else:
                kth(aux, cur, hi, k - (right - lo + 1))
        
        kth(aux, 0, len(aux) - 1, k)
        return [[x, y] for _, x, y in aux[:k]]
