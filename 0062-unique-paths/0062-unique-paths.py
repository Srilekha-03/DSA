class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    up=0
                    left=0
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=left+up
        return dp[m-1][n-1]
                    
        