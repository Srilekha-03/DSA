class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def hasZero(x):
            if x//10==0:
                return True
            y=str(x)
            l=list(y)
            if "0" in l:
                return False
            else:
                return True
        res=[]
        for i in range(1,n):
            if hasZero(i) and hasZero(n-i):
                res.append(i)
                res.append(n-i)
                break
        return res
            


        