class Solution:
    """
    2 pass (forward and backward) scan solution: 
    At each scan's cur running point, make sure closing count <= opening count, else a deletion is needed
    
    O(N)
    """
    def minRemoveToMakeValid1(self, s: str) -> str:
        def scan(string, open_char, close_char):
            res, open_cnt, close_cnt = "", 0, 0
            for c in string:
                if c ==  open_char:
                    open_cnt += 1
                elif c == close_char:
                    close_cnt += 1
                if close_cnt > open_cnt:
                    close_cnt -= 1
                else:
                    res += c
            return res
        
        tmp = scan(s, "(", ")")
        return scan(tmp[::-1], ")", "(")[::-1]
    
    """
    1 pass stack solution.
    Push indexes of opening chars into stack, pop one if we meet a closing char. If stack empty but meeting closing
    , we need to delete the current closing one. remember all the to-delte indexes and rebuild the result
    
    O(N)
    
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        index_to_del = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                index_to_del.append(i)
            else:
                stack.pop()
        to_delete = set(index_to_del + stack)
        res = []
        for i, c in enumerate(s):
            if i not in to_delete:
                res.append(c)
        return "".join(res)
        
        
