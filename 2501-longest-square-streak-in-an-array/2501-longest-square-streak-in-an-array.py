class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        length=len(nums)
        nums.sort()
        maxi=float("-inf")
        sett=set(nums)
        for i in range(length):
            res=[]
            res.append(nums[i])
            n=nums[i]
            while n**2 in sett:
                res.append(n**2)
                n=n**2
            maxi=max(maxi,len(res))
        return -1 if maxi==1 else maxi
                
        