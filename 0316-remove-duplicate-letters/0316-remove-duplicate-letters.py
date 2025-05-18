class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []    
        taken = [False] * 26
        last_index = {}     
        for i, char in enumerate(s):
            last_index[char] = i     
        for i in range(n):
            char = s[i]
            idx = ord(char) - ord('a')
            if taken[idx]:
                continue
            while stack and char < stack[-1] and last_index.get(stack[-1]) > i:
                removed_char = stack.pop()
                taken[ord(removed_char) - ord('a')] = False
            
            stack.append(char)
            taken[idx] = True
        
        return ''.join(stack)