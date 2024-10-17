class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(string):
            l, r = 0, len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def helper(pos, path, res):
            if pos == len(s):
                res.append(list(path))
            for i in range(pos + 1, len(s) + 1):
                if isPalindrome(s[pos: i]):
                    path.append(s[pos: i])
                    helper(i, path, res)
                    path.pop()
        
        path, res = [], []

        helper(0, path, res)

        return res
