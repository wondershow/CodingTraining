class TextEditor:

    def __init__(self):
        self.leftStack, self.rightStack = [], []

    def addText(self, text: str) -> None:
        for c in text:
            self.leftStack.append(c)

    def deleteText(self, k: int) -> int:
        res = 0
        while res < k and self.leftStack:
            self.leftStack.pop()
            res += 1
        return res
        

    def cursorLeft(self, k: int) -> str:
        while k > 0 and self.leftStack:
            self.rightStack.append(self.leftStack.pop())
            k -= 1
        N = len(self.leftStack)
        return "".join(self.leftStack[max(0, N - 10): N])
        

    def cursorRight(self, k: int) -> str:
        while k > 0 and self.rightStack:
            k -= 1
            self.leftStack.append(self.rightStack.pop())
        N = len(self.leftStack)
        return "".join(self.leftStack[max(0, N - 10): N])
        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
