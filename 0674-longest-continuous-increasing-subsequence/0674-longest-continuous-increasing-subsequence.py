class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi=1
        cur=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cur+=1
                maxi=max(maxi,cur)
            else:
                cur=1
        return maxi

        