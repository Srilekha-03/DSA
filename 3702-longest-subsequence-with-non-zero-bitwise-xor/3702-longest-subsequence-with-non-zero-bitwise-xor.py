class Solution:
    def longestSubsequence(self, nums):
        total_xor = 0
        all_zeros = True        
        for num in nums:
            total_xor ^= num
            if num != 0:
                all_zeros = False
                
        if all_zeros:
            return 0
        
        n = len(nums)
        if total_xor != 0:
            return n
        return n - 1