"""
Use a leftover array to hold potential unserved file contents.
Meanwhile use an eof flag to indicate if the file seek reaches end of file
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
