class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        zeroes=0
        res=0
        i=0
        for j in range(n):
            if nums[j]==0:
                zeroes+=1
            while zeroes>1:
                if nums[i]==0:
                    zeroes-=1
                i+=1
            res=max(res,j-i)
        return res
        