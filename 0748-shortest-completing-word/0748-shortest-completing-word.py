from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        res=[ch.lower() for ch in licensePlate if ch.isalpha()]
        res_count=Counter(res)
        shortest_word=None

        for word in words:
            word_count=Counter(word)
            if all(word_count[char] >= res_count[char] for char in res_count):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word=word

        return shortest_word      