
class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        res = 0
        n = len(nums)
        
        for i in range(n):
            x = lower - nums[i]
            y = upper - nums[i]
            ind1 = self.findCeil(nums, i + 1, n - 1, x)
            ind2 = self.findFloor(nums, i + 1, n - 1, y)
            
            if ind1 != -1 and ind2 != -1 and ind2 >= ind1:
                res += (ind2 - ind1 + 1)
        
        return res

    def findCeil(self, nums, low, high, x):
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def findFloor(self, nums, low, high, y):
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= y:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans