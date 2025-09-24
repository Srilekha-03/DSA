class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solve(text1,text2,0,0)
    def solve(self,s1,s2,i,j):
        if i>=len(s1) or j>=len(s2):
            return 0
        if s1[i]==s2[j]:
            return 1+self.solve(s1,s2,i+1,j+1)
        else:
            return max(self.solve(s1,s2,i,j+1),self.solve(s1,s2,i+1,j))
        