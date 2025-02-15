class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isPunishment(numstr,target,index=0,cursum=0):
            if index==len(numstr):
                return target==cursum
            for i in range(index+1,len(numstr)+1):
                part=int(numstr[index:i])
                if isPunishment(numstr,target,i,cursum+part):
                    return True
            return False

        total=0
        for i in range(1,n+1):
            square=i**2
            if isPunishment(str(square),i):
                total+=square
        return total 
         
        