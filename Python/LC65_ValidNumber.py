class Solution:
    def isNumber(self, s: str) -> bool:
        seen_dot, seen_e, seen_digit = False, False, False
        need_digit = True
        
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
                continue
            if c in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif c in "Ee":
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_dot = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit


class Solution2024:
    def isNumber(self, s: str) -> bool:
        hasDigit, hasE, hasDot, hasDigitAfterE = False, False, False, False
        for i, c in enumerate(s):
            if c in "+-":
                if i > 0 and s[i - 1] not in 'eE':
                    return False
            elif c.isdigit():
                hasDigit = True
            elif c == ".":
                if hasDot or hasE:
                    return False
                hasDot = True
            elif c in "eE": # E
                if not hasDigit or hasE:
                    return False
                hasE = True
                hasDigit = False
            else:
                return False
        return hasDigit

                
        
