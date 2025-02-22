class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def recursion(index,arr,target,dp):
            if target==0:
                return True
            if index==0:
                return arr[0]==target
            if dp[index][target]!=-1:
                return dp[index][target]
            not_take=recursion(index-1,arr,target,dp)
            take=False
            if target>=arr[index]:
                take=recursion(index-1,arr,target-arr[index],dp)
            dp[index][target]= take or not_take
            return dp[index][target]
        totalSum=0
        for i in nums:
            totalSum+=i
        if totalSum%2!=0:
            return False
        target=totalSum//2
        dp=[[-1 for i in range(target+1)]for j in range(len(nums))]
        return recursion(len(nums)-1,nums,target,dp)
        