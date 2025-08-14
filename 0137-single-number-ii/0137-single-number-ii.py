class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for k in range(32):
            countZero=0
            countOne=0
            for num in nums:
                if (num&(1<<k))==0:
                    countZero+=1                  
                else:
                    countOne+=1
            if countOne%3!=0:
                result=result|(1<<k)
        return result




        