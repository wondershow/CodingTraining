class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split("/"):
            if item == "" or item == ".":
                continue
            if item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)
