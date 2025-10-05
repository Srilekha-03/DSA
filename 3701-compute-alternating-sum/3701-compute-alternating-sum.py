class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        summ=0
        for i in range(n):
            if i%2==0:
                summ+=nums[i]
            else:
                summ-=nums[i]
        return summ

        