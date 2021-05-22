# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

"""
Standard stack solution.
TODO:
need to learn more about the "generator" method

"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
        self._move_next()
    
    def _move_next(self):
        while self.stack:
            ni_list, index = self.stack[-1]
            if index == len(ni_list):
                self.stack.pop()
            elif ni_list[index].isInteger():
                break
            else:
                next_list = ni_list[index].getList()
                self.stack[-1][1] += 1
                self.stack.append([next_list, 0])

    def next(self) -> int:
        ni_list, index = self.stack[-1]
        res = ni_list[index].getInteger()
        self.stack[-1][1] += 1
        self._move_next()
        return res
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
