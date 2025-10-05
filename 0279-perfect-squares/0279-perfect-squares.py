import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[-1]*(n+1)
        def solve(n,dp):
            if n==0:
                return 0
            if dp[n]!=-1:
                return dp[n]
            mini=float('inf')
            for i in range(1,int(math.sqrt(n))+1):
                res=1+solve(n-(i*i),dp)
                mini=min(mini,res)
            dp[n]=mini
            return dp[n]
        return solve(n,dp)
        