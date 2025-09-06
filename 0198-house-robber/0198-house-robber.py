class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2=0
        prev1=nums[0]
        for i in range(1,len(nums)):
            rob=nums[i]
            if i>1:
                rob+=prev2
            noRob=prev1
            cur=max(rob,noRob)
            prev2=prev1
            prev1=cur
        return prev1
        