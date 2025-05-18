class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)
        i = 0       
        while i < n:
            if s[i] != ' ':
                j = i
                while j < n and s[j] != ' ':
                    j += 1
                s[i:j] = s[i:j][::-1]
                i = j
            else:
                i += 1     
        return ''.join(s)
