class Solution:
    def decodeString(self, s: str) -> str:
        repeat = 0
        stack = [""]
        for c in s:
            if c.isdigit():
                repeat = repeat * 10 + int(c)
            elif c == '[':
                stack.append(repeat)
                stack.append("")
                repeat = 0
            elif c == ']':
                tmp = stack.pop() * stack.pop()
                stack[-1] += tmp
            else:
                stack[-1] += c
        return stack[0]
