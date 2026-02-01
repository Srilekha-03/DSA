class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        cost = float('inf')

        for j in range(1, n - 1):
            for k in range(j + 1, n):
                cost = min(cost, nums[0] + nums[j] + nums[k])

        return cost
        