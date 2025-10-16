class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp={}
        def helper(i,s):
            if i in dp:
                return dp[i]
            if i==n:
                return 1
            if s[i]=='0':
                return 0
            l=helper(i+1,s)
            r=0
            if i+1<n and int(s[i:i+2])<=26:
                r=helper(i+2,s)
            dp[i]=l+r
            return dp[i]
        return helper(0,s)
        