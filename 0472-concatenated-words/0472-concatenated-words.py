class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        memo = {}
        result = []
        def isConcat(word: str) -> bool:
            if word in memo:
                return memo[word]

            length = len(word)
            for i in range(1, length):  #trying all possible splits
                prefix = word[:i]
                suffix = word[i:]

                if prefix in word_set:
                    if suffix in word_set or isConcat(suffix):
                        memo[word] = True
                        return True

            memo[word] = False
            return False

        for word in words:
            word_set.remove(word)  #preventing using the word itself
            if isConcat(word):
                result.append(word)
            word_set.add(word)  #adding it back for the next iterations

        return result
