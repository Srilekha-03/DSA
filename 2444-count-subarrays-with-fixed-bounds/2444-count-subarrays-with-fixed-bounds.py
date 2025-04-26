class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        count = 0
        for i in range(len(nums)):
            mini = float('inf')
            maxi = float('-inf')
            for j in range(i, len(nums)):
                mini = min(mini, nums[j])
                maxi = max(maxi, nums[j])
                if mini == minK and maxi == maxK:
                    count += 1
        return count