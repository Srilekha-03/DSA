class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low = 1
        high = max(nums)
        
        while low <= high:
            mid = (low + high) // 2
            if self.sum_of_threshold(nums, mid) <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        
        return low

    def sum_of_threshold(self, nums, divisor):
        total = 0
        for num in nums:
            total += (num + divisor - 1) // divisor
        return total

               
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        