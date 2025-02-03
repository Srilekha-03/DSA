class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=1
        summ=0
        while j<len(nums):
            summ+=min(nums[i],nums[j])
            i+=2
            j+=2
        return summ

        