class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for val in asteroids:
            if not stack or (stack[-1] > 0 and val > 0) or (stack[-1] < 0 and val < 0) or (stack[-1] < 0 and val > 0):
                stack.append(val)
            need_to_stack = False
            while stack and stack[-1] > 0 and val < 0:
                if stack[-1] < -val:
                    need_to_stack = True
                    stack.pop()
                elif stack[-1] == -val:
                    stack.pop()
                    need_to_stack = False
                    break
                else:
                    need_to_stack = False
                    break
            if need_to_stack:
                stack.append(val)
        return stack
