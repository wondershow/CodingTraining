class Solution:
    """
    We scan s from left to right and right to left, 
    in each pass, we need to make sure at no position that closing is more than opening.
    """
    def checkValidString(self, s: str) -> bool:
        def check_valid(s, close_char):
            balance = 0
            for c in s:
                if c == close_char:
                    balance -= 1
                else:
                    balance += 1
                if balance < 0:
                    return False
            return True
        
        return check_valid(s, ")") and check_valid(s[::-1], "(")
         
