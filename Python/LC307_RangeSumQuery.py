"""
This problem needs to be re-visitd as I am not very confident on the algorithm.
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums)
        self.aux = [0] * self.N * 2
        for i in range(self.N, 2 * self.N):
            self.aux[i] = nums[i - self.N]
        for i in range(self.N - 1, 0, -1):
            self.aux[i] = self.aux[2 * i] + self.aux[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        i, delta  = self.N + index, val - self.aux[self.N + index]
        while i > 0:
            self.aux[i] += delta
            i = i // 2

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + self.N, right + self.N
        res = 0
        while l <= r:
            if l % 2 == 1:
                # if the current node [la, lb] is the right child of its parent,
                # then [la, lb] is a subset of [l ,r], we add this node to the result
                # then move l to the right which means [lb + 1, r]
                res += self.aux[l]
                l += 1
            if r % 2 == 0:
                # if the current node [ra, rb] is the left child of its parent,
                # then [ra, rb] is a subset of [l ,r], we add this node to the result
                # then move r to the left which means [l, ra - 1]
                res += self.aux[r]
                r -= 1
            l = l // 2
            r = r // 2
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
