class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        a=0
        b=nums[0]
        c=0
        for i in range(2,n+1):
            c=max(nums[i-1]+a, b)
            a=b
            b=c
        return c
