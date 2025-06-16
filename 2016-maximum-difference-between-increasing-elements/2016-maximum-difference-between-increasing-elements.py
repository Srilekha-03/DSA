class Solution(object):
    def maximumDifference(self, nums):
        n=len(nums)
        ans=-1
        mini=nums[0]
        for i in range(1,n):
            if nums[i]>mini:
                ans=max(ans,nums[i]-mini)
            mini=min(mini,nums[i])
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        