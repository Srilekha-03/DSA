class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for ch in word:
            if ch.isalpha():
                ch = ch.lower()
                if ch in 'aeiou':
                    has_vowel = True
                else:
                    has_consonant = True
            elif not ch.isdigit():
                return False

        return has_vowel and has_consonant
