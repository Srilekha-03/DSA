class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp={}
        def solve(i):
            if i>=n:
                return 0
            if i in dp:
                return dp[i]
            rob=nums[i]+solve(i+2)
            norob=solve(i+1)
            dp[i]=max(rob,norob)
            return dp[i]

        return solve(0)
        