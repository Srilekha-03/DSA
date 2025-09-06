class Solution:
    def climbStairs(self, n: int) -> int:
        t=[-1]*(n+1)
        def solve(n):
            if n<0:
                return 0
            if t[n]!=-1:
                return t[n]
            if n==0:
                return 1
            l=solve(n-1)
            r=solve(n-2)
            t[n]=l+r
            return t[n]
        return solve(n)
        