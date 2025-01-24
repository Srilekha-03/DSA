class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxones=0
        l=0
        r=0
        zeroes=0
        while r<len(nums):
            if nums[r]==0:
                zeroes+=1
            if zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            else :
                maxones=max(r-l+1,maxones)
        return


            

        