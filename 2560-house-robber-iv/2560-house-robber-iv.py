class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob(cap):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        low, high = min(nums), max(nums)
        best = high        
        while low <= high:
            mid = (low + high) // 2
            if can_rob(mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1        
        return best
        