class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n!=0:
            #to make the rightmost set bit to unset
            n=n/2
            count+=(count%2)
        return count
        