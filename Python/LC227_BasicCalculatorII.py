class Solution:
    """
    This is the dijkstra two stack method.
    1. Do some data clean up => remove space from input string
    2. when input is a number, go to number stack
    3. when input is a op, compare op with op_stack top, apply op_stack top to top 2 numbers
        until priority of current op is larger than the priority of op_stack top op
        
    Mistakes made:
    1. Use a wrap method 'do_op' to encapsulate the 'pop 2 numbers, pop 1 op_stack, apply computation, push result back to numbers stack'
    2. When the iteration is over, the last number has not been pushed to number stack it, need to do it explicitly
    """
    def calculate1(self, s: str) -> int:
        def get_priority(c):
            if c in "*/":
                return 2
            if c in "+-":
                return 1
            return 0
        
        def do_op(number_stack, operator_stack):
            right = number_stack.pop()
            left = number_stack.pop()
            op = operator_stack.pop()
            if op == "+":
                res = left + right
            elif op == "-":
                res = left - right
            elif op == "*":
                res = left * right
            else:
                res = left // right
            number_stack.append(res)
        
        s = s.replace(" ", "")
        
        numbers, operators = [], []
        val = 0
        for c in s:
            if c in "+-*/":
                numbers.append(val)
                while operators and get_priority(operators[-1]) >= get_priority(c):
                    do_op(numbers, operators)
                operators.append(c)
                val = 0
            else:
                val = val * 10 + int(c)
        numbers.append(val)
        while operators:
            do_op(numbers, operators)
        return numbers[0]
    """
    This is a "backtracking" method
    1 + 2 * 3 | * 4    
    at the current point, val = 3, res = 3 (1 + 2), pre = 2
    since we see a '*', so we deduct last section (pre) and add pre * val
    
    Note that in python, to handle division, we need to 'round towards zero' so we need to do
    int(a / b) not a// b. (exg. int(-3 / 2) = -1 while -3 // 2 = -2. The OJ accepts the  'round towards zero' result)
    """
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        index = 0
        def read_number(s):
            nonlocal index
            res = 0
            while index < len(s) and s[index].isdigit():
                res = res * 10 + int(s[index])
                index += 1
            return res
        
        pre = res = read_number(s)
        val = 0
        
        while index < len(s):
            c = s[index]
            index += 1
            num = read_number(s)
            if c == "+":
                res += num
                pre = num
            elif c == "-":
                res -= num
                pre = -num
            elif c == "*":
                res = res - pre + pre * num
                pre = pre * num
            else:
                # int(pre / num) is needed here to round results towards zero (it is python specific)
                res = res - pre + int(pre / num)
                pre = int(pre / num)
                
        return res

    def calculate(self, s: str) -> int:
        """
        This is a much easy one.
        in each iteration, we read in a number and an op,
        if the op of last iteration is "+-" push the current num onto stack,
        if the op of last iteration is "*/" do the operation between current num and stack top, then push result to the stack. 
        Finally return stack sum. 
        """
        s = s.replace(" ", "")
        stack, num, op, index = [], 0, "+", 0
        """
        Note the outmost loop can not be for loop, because within the for loop, we need to first read in a 
        number, when it is at the end of the input stream, the outer for loop will be done, the rest of the
        logic wont be carried out. 
        """
        while index < N:
            # Note that boundary check first
            while index < N and s[index].isdigit():
                cur = cur * 10 + int(s[index])
                index += 1
            if op == "+":
                stack.append(cur)
            elif op == "-":
                stack.append(-cur)
            elif op == "*":
                stack.append(cur * stack.pop())
            else:
                stack.append(int(stack.pop() / cur))
            if index < N:
                op = s[index]
                cur = 0
                index += 1
        return sum(stack)
