class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if nums[0]==nums[1]:
            return nums[0]
        if nums[n-1]==nums[n-2]:
            return nums[n-1]
        l=1
        h=len(nums)-2
        while l<=h:
            mid=l+(h-l)//2
            if nums[mid]==nums[mid-1] or nums[mid]==nums[mid+1]:
                return nums[mid]
            if mid>=nums[mid]:
                h=mid-1 
            else:
                l=mid+1
        return -1


        