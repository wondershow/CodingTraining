class Solution:
    """
    This is a dijkstra shunting yar algorithm.
    General structure:
    1. If current unit is a number push to num_stack
    2. If current unit is a "(" push to op_stack
    3. If current unit is a "+-*/":
        while op_stack top's priority >= cur unit:
            apply op_stack top's op to the top 2 num_stack numbers
            push the result to num_stack
    4. When it is a ")"
        while op_stack top is not "(":
            apply op_stack top's op to the top 2 num_stack numbers
            push the result to num_stack


    Mistakes / Tricky parts:
    1. How to know when to push a number to stack. use a 'has_number' flag. 
    2. Need to check has_number even after the outmost for loop
    3. Use int(a/b) instead of a//b to "round towards zero"
    """
    def calculate(self, s: str) -> int:
        def get_priority(c):
            if c in "*/":
                return 2
            if c in "+-":
                return 1
            return 0
        
        def do_op(number_stack, op_stack):
            right = number_stack.pop()
            left = number_stack.pop()
            op = op_stack.pop()
            if op == "+":
                number_stack.append(left + right)
            elif op == "-":
                number_stack.append(left - right)
            elif op == "*":
                number_stack.append(left * right)
            else:
                number_stack.append(int(left / right))
                
        number_stack, op_stack = [], []
        val, has_number = 0, False
        
        for i, c in enumerate(s):
            if c.isdigit():
                val = val * 10 + int(c)
                has_number = True
                continue
            if has_number:
                number_stack.append(val)
                has_number = False
                val = 0
            if c == "(":
                op_stack.append(c)
            elif c in "+-*/":
                while op_stack and get_priority(op_stack[-1]) >= get_priority(c):
                    do_op(number_stack, op_stack)
                op_stack.append(c)
            else: # ")"
                while op_stack[-1] != "(":
                    do_op(number_stack, op_stack)
                op_stack.pop()
                    
        if has_number:
            number_stack.append(val)
        while op_stack:
            do_op(number_stack, op_stack)
        return number_stack[0]
                
                
            
