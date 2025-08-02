# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        h=n
        ans=-1
        while l<=h:
            m=l+(h-l)//2
            if isBadVersion(m):
                ans=m
                h=m-1
            else:
                l=m+1
        return ans
        