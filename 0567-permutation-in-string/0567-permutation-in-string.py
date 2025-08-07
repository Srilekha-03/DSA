from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s1)
        m=len(s2)
        i=0
        j=n-1
        while j<m:
            if Counter(s1)==Counter(s2[i:j+1]):
                return True           
            i+=1
            j+=1
        return False

            

        