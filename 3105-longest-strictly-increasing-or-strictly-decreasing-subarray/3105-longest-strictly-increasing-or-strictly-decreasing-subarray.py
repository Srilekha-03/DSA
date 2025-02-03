class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        max_dec=1
        max_inc=1
        i=0
        j=1
        #increasing
        while j<len(nums):
            if nums[j]<=nums[j-1]:
                i=j
            max_inc=max(max_inc,j-i+1)
            j+=1
        #decreasing
        i=0
        j=1
        while j<len(nums):
            if nums[j]>=nums[j-1]:
                i=j
            max_dec=max(max_dec,j-i+1)
            j+=1
        maxi=max(max_inc,max_dec)
        return maxi

        
                
        