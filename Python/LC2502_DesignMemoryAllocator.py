class Allocator:

    def __init__(self, n: int):
        self.memory = [-1] * n
        self.allocation = defaultdict(list)
        

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(len(self.memory)):
            if self.memory[i] == -1:
                cnt += 1
            else:
                cnt = 0
            if cnt == size:
                self.memory[i - size + 1 : i + 1] = [mID] * size
                self.allocation[mID].extend(range(i - cnt + 1, i+1))
                return i - cnt + 1
        return -1
        

    def freeMemory(self, mID: int) -> int:
        if mID not in self.allocation:
            return 0

        res =len(self.allocation[mID])
        for i in self.allocation[mID]:
            self.memory[i] = -1
        del self.allocation[mID]
        return res
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
