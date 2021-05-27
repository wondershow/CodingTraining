class Solution:
    """
    O(N*K*N)
    """
    def kthSmallest1(self, mat: List[List[int]], k: int) -> int:
        heap, N = [], len(mat)
        
        total = sum([row[0] for row in mat if len(row) > 0])
        vector = [0] * N
        seen = {" ".join([str(a) for a in vector])}
        heap = [[total, vector]]
        for i in range(k - 1):
            total, vector = heappop(heap)
            for i in range(N):
                vector_copy = vector.copy()
                if vector_copy[i] < len(mat[i]) - 1:
                    vector_copy[i] += 1
                    signature = " ".join([str(a) for a in vector_copy])
                    if signature not in seen:
                        seen.add(signature)
                        new_total = total + mat[i][vector_copy[i]] - mat[i][vector_copy[i] - 1]
                        heappush(heap, [new_total, vector_copy])
        return heap[0][0]
    
    """
    O(KlogK*N)
    """
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def find_smallest_pairs(arr1, arr2, k):
            if not arr1 or not arr2:
                return []
            M, N = len(arr1), len(arr2)
            heap = [[arr1[0] + arr2[0], 0, 0]]
            res = []
            seen = {(0, 0)}
            for _ in range(min(M * N, k)):
                val, i, j = heappop(heap)
                res.append(val)
                if i < M - 1 and (i + 1, j) not in seen:
                    seen.add((i + 1, j))
                    heappush(heap, [arr1[i + 1] + arr2[j], i + 1, j])
                if j < N - 1 and (i, j + 1) not in seen:
                    seen.add((i, j + 1))
                    heappush(heap, [arr1[i] + arr2[j + 1], i, j + 1])
            
            return res
        
        R = len(mat)
        
        tmp = mat[0]
        
        for r in range(R - 1):
            tmp = find_smallest_pairs(tmp, mat[r + 1], k)
        return tmp[k - 1]
