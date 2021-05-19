class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse = [[i, v] for i, v in enumerate(nums) if v != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res, i, j = 0, 0, 0
        while i < len(self.sparse) and j < len(vec.sparse):
            if self.sparse[i][0] == vec.sparse[j][0]:
                res += self.sparse[i][1] * vec.sparse[j][1]
                i, j = i + 1, j + 1
            elif self.sparse[i][0] < vec.sparse[j][0]:
                i += 1
            else:
                j += 1
        return res
