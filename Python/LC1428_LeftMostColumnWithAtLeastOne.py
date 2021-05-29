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
    
    """
        Needs to practice
        put an ant at right botom, go left if cur cell is 1, 
        go up if cur cell is 0
        if row outof boundary while still at last col, -1
        else col + 1
    """
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int: 
        R, C = binaryMatrix.dimensions()
        i, j = R - 1, C - 1
        while i >=0 and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
            else:
                i -= 1
    
        if j == C - 1 and i < 0:
            return -1
        return j + 1
