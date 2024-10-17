class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {1: [], 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"], 9: ["w", "x", "y", "z"], 0: []}

        def helper(path, res, pos, digits):
            if pos == len(digits):
                res.append("".join(path))
                return
            for c in mapping[int(digits[pos])]:
                path.append(c)
                helper(path, res, pos + 1, digits)
                path.pop()
        if not digits:
            return []
        path, res = [], []
        helper(path, res, 0, digits)
        return res
