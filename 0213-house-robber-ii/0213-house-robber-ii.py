class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo = [-1] * (n - 1)
        house0 = self.solve(nums, 0, n - 1, memo)
        
        memo = [-1] * n
        lasthouse = self.solve(nums, 1, n, memo)
        
        return max(house0, lasthouse)
    
    def solve(self, nums, i, n, memo):
        if i >= n:
            return 0
        if memo[i] != -1:
            return memo[i]
        
        rob = nums[i] + self.solve(nums, i + 2, n, memo)
        notRob = self.solve(nums, i + 1, n, memo)
        
        memo[i] = max(rob, notRob)
        return memo[i]