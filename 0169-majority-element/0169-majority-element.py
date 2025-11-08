class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        n=len(nums)

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate


