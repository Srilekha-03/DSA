class Solution(object):
    def letterCombinations(self, digits):
        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return

            letters = digit_map[digits[index]]

            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        result = []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if digits:
            backtrack(0, [])

        return result
   
        