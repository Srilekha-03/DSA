class Solution:
    def triangleType(self, nums):
        nums.sort()
        valid = (nums[0] + nums[1] > nums[2])
        if not valid:
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
            return "scalene"
        else:
            return "isosceles"
