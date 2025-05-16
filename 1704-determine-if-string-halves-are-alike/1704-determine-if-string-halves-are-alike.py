class Solution:
    def isVowel(self, ch):
        return ch in 'aeiouAEIOU'
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        mid = n // 2
        countL = 0
        countR = 0
        for i in range(mid):
            if self.isVowel(s[i]):
                countL += 1
            if self.isVowel(s[i + mid]):
                countR += 1
        return countL == countR
