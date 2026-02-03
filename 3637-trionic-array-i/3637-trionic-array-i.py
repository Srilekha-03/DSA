class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        if nums[0] >= nums[1]:
            return False

        f = 1 
        c = 0  

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return False
            elif f == 1 and nums[i] <= nums[i - 1]:
                f = 0
                c += 1
            elif f == 0 and nums[i] >= nums[i - 1]:
                f = 1
                c += 1

        return c == 2 and f == 1