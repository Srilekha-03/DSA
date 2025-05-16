class Solution:
    def makeGood(self, s: str) -> str:
        result = ""       
        for ch in s:
            if (result and 
                (ord(ch) + 32 == ord(result[-1]) or 
                 ord(ch) - 32 == ord(result[-1]))):
                result = result[:-1]
            else:
                result += ch      
        return result