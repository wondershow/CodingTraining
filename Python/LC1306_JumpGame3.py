class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        visited.add(start)
        que = deque()
        que.append(start)
        N = len(arr)
        while que:
            index = que.popleft()
            if arr[index] == 0:
                return True
            if 0 <= index + arr[index] < N and index + arr[index] not in visited:
                visited.add (index + arr[index])
                que.append(index + arr[index])
            if 0 <= index - arr[index] < N and index - arr[index] not in visited:
                visited.add (index - arr[index])
                que.append(index - arr[index])
        return False
