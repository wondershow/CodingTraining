class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def format_line(arr, maxWidth):
            spaces = maxWidth - sum([len(a) for a in arr])
            if len(arr) == 1:
                return arr[0] + " " * spaces
            num_of_spaces = spaces // (len(arr) - 1)
            surplus = spaces % (len(arr) - 1)
            res = ""
            for i, word in enumerate(arr):
                res += word
                if i < len(arr) - 1:
                    res += " " * num_of_spaces
                    if i < surplus:
                        res += " "
            return res
        
        i, N = 0, len(words)
        res = []
        while i < N:
            size, j = 0, i
            while j < N:
                if size + len(words[j]) > maxWidth:
                    break
                size += len(words[j]) + 1
                j += 1
            if j < N:
                res.append(format_line(words[i:j], maxWidth))
            else:
                last_line = " ".join(words[i:j])
                last_line += " " * (maxWidth - len(last_line))
                res.append(last_line)
            i = j
        return res
