class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        d=dict()
        def solve(i,boo):
            if i>=len(nums):
                return 0
            if (i,boo) in d:
                return d[(i,boo)]
            skip=solve(i+1,boo)
            if not boo:
                val=-nums[i]
            else:
                val=nums[i]
            take=val+solve(i+1,not boo)
            d[(i,boo)]=max(skip,take)
            return d[(i,boo)]

        return solve(0,True)