class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        result = ""    
        taken = [False] * 26
        last_index = {}       
        for i, char in enumerate(s):
            last_index[char] = i
        
        for i in range(n):
            char = s[i]
            idx = ord(char) - ord('a')           
            if taken[idx]:
                continue        
            while result and char < result[-1] and last_index.get(result[-1]) > i:
                taken[ord(result[-1]) - ord('a')] = False
                result = result[:-1]          
            result += char
            taken[idx] = True
        
        return result