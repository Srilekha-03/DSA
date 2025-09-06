class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*(n+1)
        def solve(i,n,dp):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            steal=nums[i]+solve(i+2,n,dp)
            skip=solve(i+1,n,dp)
            dp[i]=max(skip,steal)
            return dp[i]
        return solve(0,n,dp)
        