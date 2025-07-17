class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    c+=1
        return c
        
        