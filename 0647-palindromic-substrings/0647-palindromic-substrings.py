class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp=[[False for i in range(n)]for j in range(n)]
        count=0
        for L in range(1,n+1):
            for i in range(0,n-L+1):
                j=i+L-1
                if i==j:
                    dp[i][j]=True
                elif s[i]==s[j]:
                    if i+1==j:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if dp[i][j]==True:
                    count+=1
        return count
        

                    



