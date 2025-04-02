class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        rightMax=[0]*n
        maxi=nums[-1]
        for i in range(n-2,0,-1):
            rightMax[i]=maxi
            maxi=max(maxi,nums[i])
        leftMax=nums[0]
        ans=0
        for i in range(1,n-1):
            ans=max(ans,(leftMax-nums[i])*rightMax[i])
            leftMax=max(leftMax,nums[i])
        return ans
            

        