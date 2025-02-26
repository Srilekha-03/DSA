class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=0
        summ=0
        for i in range(len(nums)):            
            summ+=nums[i]
            if abs(summ)<abs(nums[i]):
                summ=nums[i]
            max_sum=max(abs(summ),max_sum)
        return max_sum
        
        