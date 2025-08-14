class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n>0:
            #to make the rightmost set bit to unset
            n=n&(n-1)
            count+=1
        return count
        