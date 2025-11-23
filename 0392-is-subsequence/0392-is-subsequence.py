class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s or not t:
            return True
        i=0
        j=0
        n=len(s)
        m=len(t)
        while j<m:
            if i<n and s[i]==t[j]:
                i+=1
            j+=1
            if i==n:
                return True
        return False


            
        