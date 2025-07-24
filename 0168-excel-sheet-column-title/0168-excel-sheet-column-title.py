class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num_to_char = {i: chr(i + 64) for i in range(1, 27)}
        res=[]
        n=columnNumber
        while n>0:
            n-=1
            r=n%26
            n=n//26
            res.append(r+1)
        res[:]=res[::-1]
        return ''.join(num_to_char[r] for r in res)