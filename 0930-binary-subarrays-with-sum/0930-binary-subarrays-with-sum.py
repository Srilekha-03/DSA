class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal<0:
            return 0
        def subArrSum(nums,goal):
            l=0
            r=0
            count=0
            summ=0
            while r<len(nums):
                summ+=nums[r]
                while summ>goal and l<len(nums):
                    summ-=nums[l]
                    l+=1
                count+=r-l+1
                r+=1
            return count
        if goal == 0:
            return subArrSum(nums, goal)
        ans=subArrSum(nums,goal)-subArrSum(nums,goal-1)
        return ans

        