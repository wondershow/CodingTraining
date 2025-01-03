class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = ([], [])
        self.keys[key][0].append(value)
        self.keys[key][1].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        index = bisect_left(self.keys[key][1], timestamp)
        #N = len(self.keys[key])
        print(f'get {key} {timestamp} index = {index}')
        if index == len(self.keys[key][0]):
            print("a")
            return self.keys[key][0][-1]
        elif index == 0 and timestamp < self.keys[key][1][0]:
            print("b")
            return ""
        elif timestamp < self.keys[key][1][index]:
            return self.keys[key][0][index - 1]
        else:
            return self.keys[key][0][index]


class TimeMap:

    def __init__(self):
        """
        Look at this much more concise one:
        Note that bisect is the same as bisect_right
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        index = bisect.bisect(self.store[key], [timestamp, chr(127)])
        if index == 0:
            return ""
        return self.store[key][index - 1][1]
            



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
