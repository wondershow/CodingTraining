class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.val_index = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_index:
            return False
        self.val_index[val] = len(self.values)
        self.values.append(val)
        return True    
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_index:
            return False
        last_index, index = len(self.values) - 1, self.val_index[val]
        last_val = self.values[last_index]
        self.values[index], self.values[last_index] = self.values[last_index], self.values[index]
        self.values.pop()
        self.val_index[last_val] = index
        del self.val_index[val]
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
