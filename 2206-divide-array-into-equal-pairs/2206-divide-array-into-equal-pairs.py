from collections import Counter 
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        h=Counter(nums)
        for val,count in h.items():
            if count%2!=0:
                return False
        return True


        