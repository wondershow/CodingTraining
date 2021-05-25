class Solution:
    """
    Mistakes made:
    1. Failed to conver word[0] to lower
    """
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        res = []
        for i, word in enumerate(words):
            if word[0].lower() in "aeiou":
                res.append(word + "ma" + "a" * (i + 1))
            else:
                res.append(word[1:] + word[0] + "ma" + "a" * (i + 1))
        return " ".join(res)
