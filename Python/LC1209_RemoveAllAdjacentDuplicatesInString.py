class Solution:
    """
    This is a stack problem
    Mistakes made
    instead of using endswith(c) I used stack[-1] == c, which stack[-1] could be "aaaa" and c is "a", so this is a tweak.
    """
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            # We need to say stack[-1][-1] not stack[-1]
            if stack and stack[-1].endswith(c):
                stack[-1] += c
                if len(stack[-1]) % k == 0:
                    stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
