class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        countCapitals = 0
        for ch in word:
            if ch.isupper():
                countCapitals += 1
        if countCapitals == 0:
            return True
        if countCapitals == len(word):
            return True
        if countCapitals == 1 and word[0].isupper():
            return True
        return False
