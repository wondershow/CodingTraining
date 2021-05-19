class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res, stack = [0] * n, []
        for log in logs:
            tmp = log.split(":")
            index, action, timestamp = int(tmp[0]), tmp[1], int(tmp[2])
            if action == "start":
                if stack:
                    res[stack[-1][0]] +=  timestamp - stack[-1][1]
                stack.append([index, timestamp])
            else:
                index, start_time = stack.pop()
                res[index] += timestamp + 1 - start_time
                if stack:
                    stack[-1][1] = timestamp + 1
        return res
