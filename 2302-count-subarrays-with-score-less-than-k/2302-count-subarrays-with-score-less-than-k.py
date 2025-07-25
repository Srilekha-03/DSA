class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        left = 0
        current_sum = 0 
        right=0     
        while right<n:
            current_sum += nums[right]
            while left <= right and current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            count += (right - left + 1) 
            right+=1      
        return count