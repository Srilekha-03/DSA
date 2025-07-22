from collections import defaultdict
class Solution:
    def findRoot(self, word: str, root_set: set) -> str:
        for l in range(1, len(word) + 1):
            root = word[:l]
            if root in root_set:
                return root
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)

        words = sentence.split()
        result = []

        for word in words:
            result.append(self.findRoot(word, root_set))

        return " ".join(result)
