class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeroes = 0
        maxones = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            maxones = max(maxones, r - l + 1)
        
        return maxones


            

        