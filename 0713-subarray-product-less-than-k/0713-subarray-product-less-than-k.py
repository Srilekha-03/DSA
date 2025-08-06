class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        n=len(nums)
        i=0
        j=0
        count=0
        product=1
        while j<n:
            product*=nums[j]
            while product>=k:
                product//=nums[i]
                i+=1
            count+=(j-i+1)
            j+=1
        return count
        