class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        nums=sorted(set(nums))
        if min(nums)==k:
            return len(nums)-1
        if min(nums)>k:
            return len(nums)        