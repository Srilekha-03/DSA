from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms=permutations(nums)
        unique=set(perms)
        return [list(i) for i in unique]

        