class Solution(object):
    def searchInsert(self, nums, x):
        n=len(nums)
        ans=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
                
        return ans
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        