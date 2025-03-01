class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1]=2*nums[i-1]
                nums[i]=0
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                if i!=j:
                    nums[i]=0
                j+=1
        return nums
        