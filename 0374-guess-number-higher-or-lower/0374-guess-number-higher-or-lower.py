# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        h=n
        ans=-1
        while l<=h:
            m=l+(h-l)//2
            if guess(m)==0:
                ans=m
                return ans
            if guess(m)==-1:
                h=m-1
            else:
                l=m+1
        return ans
        