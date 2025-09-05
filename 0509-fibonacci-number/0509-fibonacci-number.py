class Solution:
    def fib(self, n: int) -> int:
        dp=[0]*(n+1)
        def fibonacci(n):
            if n<2:
                return n
            if dp[n]!=0:
                return dp[n]
            dp[n]=fibonacci(n-1)+fibonacci(n-2)
            return dp[n]
        ans=fibonacci(n)
        return ans

        