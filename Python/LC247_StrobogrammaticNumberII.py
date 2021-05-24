class Solution:
    """
    The example of this case is confusing, which may trick you think the n = 2 case to be a basic case of recursion.
    instead of using n = 1 and n =2 , we need to use n = 0 and n =1 as basic use cases.
    
    We need to pass in two variables into recursion (start, cur)
    start means the outmost level, cur means the current level
    when cur != start, 
        that means we can wrap 0 outside of last level's result, elg. 69 => 0690
    
    """
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(start, cur):
            if cur == 0:
                return [""]
            if cur == 1:
                return ["0","1","8"]
            last_level = helper(start, cur - 2)
            res = []
            for item in last_level:
                res.append("1" + item + "1")
                res.append("8" + item + "8")
                res.append("6" + item + "9")
                res.append("9" + item + "6")
                if cur != start:
                    res.append("0" + item + "0")
            return res
        return helper(n, n)
