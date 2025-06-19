class Solution(object):
    def partitionArray(self, nums, k):
        nums.sort()
        n=len(nums)
        count=1
        mini=nums[0]
        for i in range(n):
            if nums[i]-mini>k:
                count+=1
                mini=nums[i]
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        