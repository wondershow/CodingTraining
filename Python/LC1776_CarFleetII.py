class Solution:
    """
    Scan from right to left, we use a stack to keep all the vehciels that from slow to fast (stack top is the fastest). At each iteration, if the current vehicle speed is slower than the stack top vehicle, that means the current vehicle will never catch up with the stack top vehicle, pop stack.
    
    """
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        def get_collison_time(s1, p1, s2, p2):
            return (p2 - p1) / (s1 - s2) 
        
        N = len(cars)
        res, stack = [-1] * N, []
        for i in range(N - 1, -1, -1):
            while stack:
                pos, speed = cars[i]
                if speed <= cars[stack[-1]][1]:
                    stack.pop()
                elif res[stack[-1]] > 0 and get_collison_time(speed, pos, cars[stack[-1]][1], cars[stack[-1]][0]) > res[stack[-1]]:
                    stack.pop()
                else:
                    break
            if stack:
                res[i] = get_collison_time(speed, pos, cars[stack[-1]][1], cars[stack[-1]][0])
            else:
                res[i] = -1
            stack.append(i)
        return res
        
