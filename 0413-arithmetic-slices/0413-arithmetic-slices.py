class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        cur=0
        for i in range(2,n):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                cur+=1
                c+=cur
            else:
                cur=0
        return cur
            