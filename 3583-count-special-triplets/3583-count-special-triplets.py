class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        
        left = {}
        right = {}

        for x in nums:
            right[x] = right.get(x, 0) + 1
            
        ans = 0
        
        for j in range(len(nums)):
            center = nums[j]

            right[center] -= 1
            if right[center] == 0:
                del right[center]
            
            target = center * 2
            
            left_count = left.get(target, 0)
            right_count = right.get(target, 0)
            
            ans += (left_count * right_count)
            ans=ans%MOD

            left[center] = left.get(center, 0) + 1
        
        return ans