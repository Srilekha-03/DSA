class Solution(object):
    def maxAdjacentDistance(self, nums):
        n=len(nums)
        maxd=float('-inf')
        for i in range(1,n):
            maxd=max(abs(nums[i]-nums[i-1]),abs(nums[i-1]-nums[i]))
        maxd=max(maxd,abs(nums[0]-nums[-1]),abs(nums[-1]-nums[0]))
        return maxd


        """
        :type nums: List[int]
        :rtype: int
        """
        