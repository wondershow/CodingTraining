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
        i = j
        return res

    def fullJustify1(self, words: List[str], maxWidth: int) -> List[str]:
        """
        This one is much concise and elegant.
        """
        currentLine, numLetters, result = [], 0, []
        for word in words:
            if len(currentLine) + len(word) + numLetters > maxWidth:
                if len(currentLine) == 1:
                    currentLine[0] += " " * (maxWidth - len(currentLine[0]))
                else:
                    for i in range(maxWidth - numLetters):
                        currentLine[i % (len(currentLine) - 1)] += " "
                result.append("".join(currentLine))
                currentLine, numLetters = [], 0
            currentLine.append(word)
            numLetters += len(word)

        lastLine = " ".join(currentLine)
        lastLine += " " * (maxWidth - len(lastLine))
        result.append(lastLine)
        return result
