class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        nums.sort()
        lis = 1
        dp = [1] * n       
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    if lis < dp[i]:
                        lis = dp[i]
        prev = -1
        for i in range(n - 1, -1, -1):
            if dp[i] == lis and (prev == -1 or prev % nums[i] == 0):
                ans.append(nums[i])
                lis -= 1
                prev = nums[i]       
        return ans