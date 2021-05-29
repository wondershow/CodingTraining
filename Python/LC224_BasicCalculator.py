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
                
                
                
