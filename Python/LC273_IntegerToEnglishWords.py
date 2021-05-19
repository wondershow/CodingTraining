class Solution:
    def numberToWords(self, num: int) -> str:
        under20 = {1 : "One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6: "Six", 7: "Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11: "Eleven", 12:"Twelve", 13: "Thirteen", 14:"Fourteen", 15: "Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen"}
        tens = {20 : "Twenty", 30: "Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70: "Seventy", 80:"Eighty", 90:"Ninety"}
        if num == 0:
            return "Zero"
        if num < 20:
            return under20[num]
        if num < 100:
            res = tens[(num // 10) * 10]
            if num % 10 == 0:
                return res
            return res + " " + under20[num % 10]
        if num < 1000:
            hundred = num // 100
            res = under20[num // 100] + " Hundred"
            if num % 100 == 0:
                return res
            return res + " " + self.numberToWords(num % 100)
        if num < 10 ** 6:
            thousand = num // 1000
            res = self.numberToWords(num // 1000) + " Thousand"
            if num % 1000 == 0:
                return res
            return res + " " + self.numberToWords(num % 1000)
        if num < 10 ** 9:
            million = num // (10 ** 6)
            res = self.numberToWords(num // (10 ** 6)) + " Million"
            if num % (10**6) == 0:
                return res
            return res + " " + self.numberToWords(num % (10**6))
        billion = num // (10 ** 9)
        res = self.numberToWords(num // (10 ** 9)) + " Billion"
        if num % (10**9) == 0:
            return res
        return res + " " + self.numberToWords(num % (10**9))
