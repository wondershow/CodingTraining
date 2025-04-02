class LFUCache(object):
    """
    Foudations:
    For Python, there is a builtin DS called OrderedDict which is similar to LinkedHashMap of Java. This DS
    preserves the order of operations on a set/map. This way we can easily remove the oldest item on in OD or
    a random item in an OD with O(1) time complexity.

    For this problem, we maintain 4 instance variables:
    1. Freq -> OD {[key, val]}
    2. key -> (freq, val)
    3. minFreq
    4. size

    The rest of the work needs patience and carefulness. 
    """

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.minFreq = 0
        self.keyValDictByFreq = {}
        self.freqValByKey = {}
        self.size = 0
        self.cap = capacity

    def _addKeyValWithFreq(self, key, val, freq):
        self.freqValByKey[key] = (freq, val)
        if freq not in self.keyValDictByFreq:
            self.keyValDictByFreq[freq] = OrderedDict()
        self.keyValDictByFreq[freq][key] = val
    
    def _delKeyValWithFreq(self, key, val, freq):
        del self.freqValByKey[key]
        tmp = self.keyValDictByFreq[freq]
        del tmp[key]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.freqValByKey:
            return -1
        freq, val = self.freqValByKey[key]
        self._delKeyValWithFreq(key, val, freq)
        self._addKeyValWithFreq(key, val, freq + 1)
        if len(self.keyValDictByFreq[freq]) == 0 and freq == self.minFreq:
            self.minFreq += 1
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.freqValByKey:
            if self.size == self.cap:
                minFreqUnit = self.keyValDictByFreq[self.minFreq]
                oldestKey = next(iter(minFreqUnit))
                oldestVal = self.keyValDictByFreq[self.minFreq][oldestKey]
                self._delKeyValWithFreq(oldestKey, oldestVal, self.minFreq)
                self.size -= 1
            self._addKeyValWithFreq(key, value, 1)
            self.minFreq = 1
            self.size += 1
        else:
            oldFreq, oldVal = self.freqValByKey[key]
            self._delKeyValWithFreq(key, oldVal, oldFreq)
            self._addKeyValWithFreq(key, value, oldFreq + 1)
            if len(self.keyValDictByFreq[oldFreq]) == 0 and oldFreq == self.minFreq:
                self.minFreq += 1






# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
