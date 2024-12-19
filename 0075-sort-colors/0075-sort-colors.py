class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        low=0
        mid=0
        high=n-1
        while (mid<=high):
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        