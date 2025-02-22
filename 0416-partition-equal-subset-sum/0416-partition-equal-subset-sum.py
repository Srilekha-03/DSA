class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def tabulation(arr, target):
            dp=[[0 for i in range(target+1)]for j in range(len(arr))]
            for i in range(len(arr)):
                dp[i][0]=True
            if arr[0] <= target:
                dp[0][arr[0]]=True
            for index in range(1,len(arr)):
                for targ in range(target+1):
                    not_take=dp[index-1][targ]
                    take=False
                    if target>=arr[index]:
                        take=dp[index-1][targ-arr[index]]
                    dp[index][targ]=take or not_take
            return dp[len(arr)-1][target]
        totalSum=0
        for i in nums:
            totalSum+=i
        if totalSum%2!=0:
            return False
        target=totalSum//2
        dp=[[-1 for i in range(target+1)]for j in range(len(nums))]
        return tabulation(nums,target)
        