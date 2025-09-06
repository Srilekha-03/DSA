class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp=[-1]*(n+1)

        def solve(i,n,dp):
            if i>n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            rob=nums[i]+solve(i+2,n,dp)
            norob=solve(i+1,n,dp)
            dp[i]=max(rob,norob)
            return dp[i]

        result1=solve(0,n-2,dp)
        dp=[-1]*(n+1)
        result2=solve(1,n-1,dp)
        return max(result1,result2)