class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=1
        maxi=2
        count=2
        while j<n-1:
            if nums[i]+nums[j]==nums[j+1]:
                count+=1
                maxi=max(maxi,count)
            else:
                count=2
            i+=1
            j+=1
        return maxi


        