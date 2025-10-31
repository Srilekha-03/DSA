class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        self.mem=dict()
        return self.solve(0,0,text1,text2,n,m)
    def solve(self,i,j,t1,t2,n,m):
        if i>=n or j>=m:
            self.mem[(i,j)]=0
            return self.mem[(i,j)]
        if (i,j) in self.mem:
            return self.mem[(i,j)]
        if t1[i]==t2[j]:
            self.mem[(i,j)]=1+self.solve(i+1,j+1,t1,t2,n,m)
            return self.mem[(i,j)]
        self.mem[(i,j)]=max(self.solve(i,j+1,t1,t2,n,m),self.solve(i+1,j,t1,t2,n,m))
        return self.mem[(i,j)]