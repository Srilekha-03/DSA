class Solution:
    def arrangeCoins(self, n: int) -> int:
        l=0
        h=n
        ans=-1
        while l<=h:
            m=l+(h-l)//2
            if m*(m+1)//2<=n:
                ans=m
                l=m+1
            else:
                h=m-1
        return ans
        