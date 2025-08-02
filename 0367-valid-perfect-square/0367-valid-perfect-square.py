class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        h=num
        while l<=h:
            m=l+(h-l)//2
            if m*m==num:
                return True
            elif m*m>num:
                h=m-1
            else:
                l=m+1
        return False

        