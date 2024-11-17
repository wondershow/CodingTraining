class UF:
    def __init__(self, size):
        self.uf = [i for i in range(size)]
        self.size = [1 for _ in range(size)]
        self.max_size = 1

    def root(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.root(self.uf[x])
        return self.uf[x]

    def union(self, a, b):
        r1, r2 = self.root(a), self.root(b)
        if r1 != r2:
            self.uf[r1] = r2
            self.size[r2] += self.size[r1]
            self.max_size = max(self.size[r2], self.max_size)

    def max_component_size(self):
        return self.max_size

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        uf = UF(size)
        index_by_val = {}
        for i, num in enumerate(nums):
            # skip duplicates
            if num in index_by_val:
                continue
            if (num + 1) in index_by_val:
                uf.union(i, index_by_val[num + 1])
            if (num - 1) in index_by_val:
                uf.union(i, index_by_val[num - 1])
            index_by_val[num] = i
        return uf.max_component_size()
