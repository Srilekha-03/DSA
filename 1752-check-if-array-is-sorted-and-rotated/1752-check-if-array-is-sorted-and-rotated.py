class Solution(object):
    def check(self, nums):
        count_breaks = 0 
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count_breaks += 1
            
        
            if count_breaks > 1:
                return False
        
        return True

        