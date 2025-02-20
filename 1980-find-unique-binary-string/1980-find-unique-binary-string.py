class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n= len(nums)
        return ''.join('1' if nums[i][i] == '0' else '0' for i in range(n))
        