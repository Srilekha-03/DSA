class Solution(object):
    def search(self, nums, target):
        n=len(nums)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            if nums[low]==nums[mid] and nums[high]==nums[mid]:
                low+=1
                high-=1
                continue
            if nums[low]<=nums[mid]:
                if  nums[low]<=target and target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<=target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        