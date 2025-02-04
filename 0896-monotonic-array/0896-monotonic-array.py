class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if not self.monoinc(nums) and not self.monodec(nums):
            return False
        return True
    def monoinc(self,nums):
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return False
        return True
    def monodec(self,nums):
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                return False
        return True
        