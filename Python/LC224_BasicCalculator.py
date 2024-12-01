class Solution:
    """
    We use a Dijkstra shunting yard algorithm with a little variable (due to the special input case of this problem)
    When we see a '+' or '-', it does not necessary need to be an operator. Since we can have '-3 + 2'
    or '3 - (+7-2)'. To accomodate this case in regular shunting yard, we need when we see '+' or '-'
    preceding with '(' or at index 0, we know that operator has no explicit left operand. So we implicitly add a number 0 to the number stack and then push the operator into op stack.
    """
    def calculate(self, s: str) -> int:
        def do_op(num_stack, op_stack):
            right = num_stack.pop()
            left = num_stack.pop()
            op = op_stack.pop()
            if op == "+":
                num_stack.append(left + right)
            else:
                num_stack.append(left - right)
        s = s.replace(" ", "")
        op_stack, num_stack = [], []
        has_number, val, sign = False, 0, 1
        for i, c in enumerate(s):
            if c.isdigit():
                val = val * 10 + int(c)
                has_number = True
                continue
            if has_number:
                num_stack.append(val * sign)
                val, has_number, sign = 0, False, 1
            if c == "(":
                op_stack.append(c)
            elif c in "+-":
                if i == 0 or s[i - 1] not in "0123456789)":
                    op_stack.append(c)
                    num_stack.append(0)
                else:
                    while op_stack and op_stack[-1] != "(":
                        do_op(num_stack, op_stack)
                    op_stack.append(c)
            elif c == ")":
                while op_stack[-1] != "(":
                    do_op(num_stack, op_stack)
                op_stack.pop()
        if has_number:
            num_stack.append(val*sign)
        while op_stack:
            do_op(num_stack, op_stack)
        #print(str(len(num_stack)))
        return num_stack[0]

def calculate1(self, s: str) -> int:
        """
        This method seems to be much easier.
        We scan left to right, 
        cur -> current number
        sign -> last sign (+ or -)
        res -> the result of current level (save parenthesis)
        stack is used to track the nested case. 
        When there is a "(", we push 2 items onto the stack, the current sum until the "("
        and the sign (+ or -) right before the "(".

        When there is a ")", first add cur to  res, then times it with the stack top, 
        then add to the next stack top.

        1 + 4 - (8 + 7 - 3)
                 | [0, 1, 5, -1]    

        """
        stack, res, cur, sign = [], 0, 0, 1
        for c in s:
            if c.isdigit():
                cur = (cur * 10) + int(c)
            elif c in "+-":
                res += cur * sign
                cur = 0
                if c == "+":
                    sign = 1
                else:
                    sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                cur, res = 0, 0
                sign = 1
            elif c == ")":
                res += cur * sign
                res *= stack.pop()
                res += stack.pop()
                cur = 0
        return res + cur * sign
                
                
