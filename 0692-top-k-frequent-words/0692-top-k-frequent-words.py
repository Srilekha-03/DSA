from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=Counter(words)
        # First sort alphabetically
        sorted_words = sorted(freq.keys())

        # Then sort by frequency (descending), stable keeps alphabetical order for ties
        sorted_words = sorted(sorted_words, key=lambda w: freq[w], reverse=True)
        return sorted_words[:k]


        