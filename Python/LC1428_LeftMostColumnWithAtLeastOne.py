"""
    Understand the boundary condition and move legs correctly.
    O(RlogC)
    """
    def leftMostColumnWithOne1(self, binaryMatrix: 'BinaryMatrix') -> int:
        def column_has_one(binaryMatrix, col, R):
            for i in range(R):
                if binaryMatrix.get(i, col) == 1:
                    return True
            return False
        
        R, C = binaryMatrix.dimensions()
        
        lo, hi = 0, C - 1
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if column_has_one(binaryMatrix, mid, R):
                hi = mid
            else:
                lo = mid + 1
        
        if column_has_one(binaryMatrix, lo, R):
            return lo
        if column_has_one(binaryMatrix, hi, R):
            return hi
        
        return -1
