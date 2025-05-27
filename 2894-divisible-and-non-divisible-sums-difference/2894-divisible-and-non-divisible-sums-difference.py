class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s1=0
        s2=0
        for i in range(1,n+1):
            if i%m!=0:
                s1+=i
        for i in range(1,n+1):
            if i%m==0:
                s2+=i
        return s1-s2