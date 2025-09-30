class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        while len(nums) > 1:
            new = []
            for i in range(len(nums) - 1):
                new.append((nums[i] + nums[i+1]) % 10)
            nums = new 
        return nums[0]
        