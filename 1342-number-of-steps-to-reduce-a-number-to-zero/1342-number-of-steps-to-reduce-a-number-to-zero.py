class Solution:
    def numberOfSteps(self, num: int) -> int:
        def count(num,c):
            if num==0:
                return c 
            if num%2==0:
                return count(num/2,c+1)
            else:
                return count(num-1,c+1)
        ans=count(num,0)
        return ans
        