class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isValidSection(section: str):
            if section.startswith("0") and len(section) > 1:
                return False
            if int(section) > 255:
                return False
            return True

        def helper(pos, path, res):
            if pos == len(s) or len(path) > 4:
                if len(path) == 4 and pos == len(s):
                    res.append(".".join(path))
                return
                # Here i needs to be from [pos + 1, post + 4)
            for i in range(pos + 1, min(pos + 4, len(s) + 1)):
                if isValidSection(s[pos: i]):
                    path.append(s[pos: i])
                    helper(i, path, res)
                    path.pop()
        res = []
        helper(0, [], res)
        return res
