class Solution:
    def checkEqualPartitions(self, nums, target: int) -> bool:
        return self.helper(0, 1, 1, nums, target)

    def helper(self, ind: int, p1: int, p2: int, nums: list[int], t: int) -> bool:
        if ind >= len(nums):
            return p1 == t and p2 == t
        
        if self.helper(ind + 1, p1 * nums[ind], p2, nums, t):
            return True
        
        if self.helper(ind + 1, p1, p2 * nums[ind], nums, t):
            return True

        return False