class Solution:
    MOD = 10**9 + 7
    def countHomogenous(self, s: str) -> int:
        result = 0
        count = 0        
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                count += 1
            else:
                count = 1          
            result = (result + count) % self.MOD    
        return result
