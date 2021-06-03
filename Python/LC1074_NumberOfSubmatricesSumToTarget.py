class Solution:
    """
        The key of this problem is how to convert a 2D problem into 1D.
        
        
        f(i,j) = sum of submatrix from (0,0) to (i - 1, j - 1)
        
        for a matrix (r1, c1) to (r2, c2)
        its sum can be expressed as : sum ([r1, 0], [r2, c2]) - sum([r1, 0], [r2, c1 - 1])
        sum ([r1, 0], [r2, c2]) = f()
        
        So the overall roadmap is we enumerate different combinations of r1, r2, then
        we compute the summatrix sum between r1, r2 (it is a 1d problem)
        
        Mistakes made:
        1. it is not running_sum += anymore, running_sum[i][j] can be computed  by 2d prefix sum
        2. it is 'running_sum - target' key check, not 'target - running_sum'
        
    """
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        M, N = len(matrix), len(matrix[0])
        ps2d = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                ps2d[i][j] = matrix[i - 1][j - 1] + ps2d[i - 1][j] + ps2d[i][j - 1] - ps2d[i - 1][j - 1]
        
        #for line in ps2d:
        #    print (" ".join([str(a) for a in line]))
        
        res = 0
        for r1 in range(1, M + 1):
            for r2 in range(r1, M + 1):
                seen = defaultdict(int)
                seen[0], running_sum = 1, 0
                
                for c in range(1, N + 1):
                    
                    # 2nd error
                    running_sum = ps2d[r2][c] - ps2d[r1 - 1][c]
                    
                    # First error
                    res += seen[running_sum - target]
                    seen[running_sum] += 1
        return res
