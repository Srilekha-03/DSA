class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.insert(i+1,0)
                nums.pop()
                i+=2
            else:
                i+=1

        """
        Do not return anything, modify arr in-place instead.
        """
        