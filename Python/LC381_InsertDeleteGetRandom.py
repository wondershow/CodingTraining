import random
class RandomizedCollection:

    def __init__(self):
        self.index_by_val = defaultdict(set)
        self.values = []
        

    def insert(self, val: int) -> bool:
        res = True
        if val in self.index_by_val:
            res = False
        self.values.append(val)
        self.index_by_val[val].add(len(self.values) - 1)
        return res

    def remove(self, val: int) -> bool:
        if val not in self.index_by_val:
            return False
        index = self.index_by_val[val].pop()
        size = len(self.values)
        last_val = self.values[-1]
        self.values[index], self.values[size - 1] = self.values[size - 1], self.values[index]
        self.index_by_val[last_val].add(index)
        self.index_by_val[last_val].remove(size - 1)
        if len(self.index_by_val[val]) == 0:
            del self.index_by_val[val]
        
        self.values.pop()
        return True

    def getRandom(self) -> int:
        size = len(self.values)
        return self.values[random.randint(0, size - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
