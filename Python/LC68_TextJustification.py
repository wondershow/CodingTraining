class Solution:
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
