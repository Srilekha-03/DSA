from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=Counter(nums)
        for key in d.keys():
            if d[key]==1:
                return key


