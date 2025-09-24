class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        maxi=float("-inf")
        for i in range(n):
            res=[]
            res.append(nums[i])
            n=nums[i]
            while n**2 in nums:
                res.append(n**2)
                n=n**2
            maxi=max(maxi,len(res))
        return -1 if maxi==1 else maxi
                
        