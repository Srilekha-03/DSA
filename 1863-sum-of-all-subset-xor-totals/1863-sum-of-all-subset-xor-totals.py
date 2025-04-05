class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        return self.subset(nums, 0, 0)

    def subset(self, nums: list[int], i: int, xor: int) -> int:
        if i == len(nums):
            return xor
        with_curr = self.subset(nums, i + 1, xor ^ nums[i])
        without_curr = self.subset(nums, i + 1, xor)
        return with_curr + without_curr
