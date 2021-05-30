"""
Use a leftover array to hold potential unserved file contents.
Meanwhile use an eof flag to indicate if the file seek reaches end of file

The first method might be easire to understand with an EOF flag
"""
class Solution:
    def __init__(self):
        self.leftover = []
        self.eof = False
    
    def read(self, buf: List[str], n: int) -> int:
        count = 0
        while count < n and not self.eof:
            if len(self.leftover) > 0:
                buf[count] = self.leftover.pop(0)
                count += 1
            else:
                self.leftover = [" "] * 4
                arrival = read4(self.leftover)
                #print(self.leftover)
                if arrival == 0:
                    self.eof = True
                    break
                while arrival < 4:
                    self.leftover.pop()
                    arrival += 1
        return count
    
    def _refill(self):
        self.left_over = [" "] * 4
        delta = read4(self.left_over)
        while delta < 4:
            self.left_over.pop()
            delta += 1
        
    def read1(self, buf: List[str], n: int) -> int:
        count = 0
        while count < n:
            while count < n and len(self.left_over) > 0:
                buf[count] = self.left_over.pop(0)
                count += 1
            if count == n:
                break
            self._refill()
            if len(self.left_over) == 0:
                break
        return count
