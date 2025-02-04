from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        first={}
        last={}
        for i, val in enumerate(nums):
            if val not in first:
                first[val] = i
            last[val] = i
        min_length = float('inf')
        for num in freq:
            if freq[num] == max_freq:
                min_length = min(min_length, last[num] - first[num] + 1)

        return min_length


    
        