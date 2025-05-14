class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        found = False
        i = 0
        n = len(word)       
        for i in range(n):
            letter = word[i]
            stack.append(letter)
            if ch == letter:
                found = True
                break
        if found:
            ans = ''
            while stack:
                ans += stack.pop()
            ans += word[i+1:]
            return ans
        return word