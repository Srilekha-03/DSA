class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=max(nums)
        count=0
        max_len=float('-inf')
        for i in range(len(nums)):
            if nums[i]==maxi:
                count+=1
                max_len=max(max_len,count)
            else:
                count=0
        return max_len
        