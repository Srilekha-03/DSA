class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = nums[0]
        min_product = nums[0]
        max_product = nums[0]
        for i in range(1, len(nums)):
            temp_min = min(nums[i], min_product * nums[i], max_product * nums[i])
            temp_max = max(nums[i], min_product * nums[i], max_product * nums[i]) 
            min_product = temp_min
            max_product = temp_max 
            ans = max(ans, max_product, min_product)

        return ans


        