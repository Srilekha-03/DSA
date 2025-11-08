class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        k=2
        for j in range(2,n):
            if nums[j]!=nums[k-2]:
                nums[k]=nums[j]
                k+=1
        return k
            

        