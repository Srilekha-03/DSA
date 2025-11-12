class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        word_to_char = {}
        used_chars = set()
        for w, p in zip(words, pattern):
            if w not in word_to_char:
                if p in used_chars:
                    return False
                word_to_char[w] = p
                used_chars.add(p)
            else:
                if word_to_char[w] != p:
                    return False
        return True
