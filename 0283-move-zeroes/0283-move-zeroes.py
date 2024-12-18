class Solution(object):
    def moveZeroes(self, nums):
        j=-1
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                j=i
                break
        if j!=-1:
            for i in range(j+1,n):
                if nums[j]!=nums[i]:
                    nums[j],nums[i]=nums[i],nums[j]
                    j+=1
        return nums
            

                
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        