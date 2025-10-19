class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num=set(nums)
        for i in range(k,200,k):
            if i!=0 and i not in nums:
                return i
        return -1
        