class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()   
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for c, w in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                if w in word_to_char:
                    return False
                char_to_word[c] = w
                word_to_char[w] = c
        return True
        