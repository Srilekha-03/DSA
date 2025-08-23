class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=0
        summ=0
        maxi=float('inf')
        while j<n:
            summ+=nums[j]
            while summ>=target:
                maxi=min(maxi,j-i+1)
                summ-=nums[i]
                i+=1
            j+=1
        return maxi if maxi!=float('inf') else 0

        