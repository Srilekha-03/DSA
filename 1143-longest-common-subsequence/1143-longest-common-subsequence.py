class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp={}
        return self.solve(n-1,m-1,text1,text2,dp)
    def solve(self,n,m,text1,text2,dp):
        if n<0 or m<0:
            return 0
        if (n,m) in dp:
            return dp[(n,m)]
        if text1[n]==text2[m]:
            dp[(n,m)]=1+self.solve(n-1,m-1,text1,text2,dp)
            return dp[(n,m)]
        else:
            dp[(n,m)]=max(self.solve(n-1,m,text1,text2,dp),self.solve(n,m-1,text1,text2,dp))
            return dp[(n,m)]
        