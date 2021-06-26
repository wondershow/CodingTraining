class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        for i in range(10):
            my_guess = random.choice(wordlist)
            x = master.guess(my_guess)
            wordlist = [word for word in wordlist if sum([a == b for a, b in zip(word, my_guess)]) == x]
