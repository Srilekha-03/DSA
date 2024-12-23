class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        low=1
        high=n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2!=0 and nums[mid]==nums[mid-1]):
                low=mid+1
            else:
                high=mid-1
        return -1


        """
        :type nums: List[int]
        :rtype: int
        """
        