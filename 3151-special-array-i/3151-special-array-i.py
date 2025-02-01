class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i=0
        j=1
        while j<len(nums):
            if nums[i]%2==0 and nums[j]%2==0:
                return False
            if nums[i]%2==1 and nums[j]%2==1:
                return False
            i+=1
            j+=1
        return True

        