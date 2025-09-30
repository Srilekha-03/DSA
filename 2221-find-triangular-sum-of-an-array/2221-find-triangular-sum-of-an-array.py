class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return self.solve(nums)
    def solve(self,nums):
        if len(nums)==1:
            return nums[0]
        new=[0]*(len(nums)-1)
        for i in range(len(nums)-1):
            new[i]=(nums[i]+nums[i+1])%10
        return self.solve(new)
        