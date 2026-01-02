class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums) // 2
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == n:
                return num