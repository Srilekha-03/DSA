class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        n = len(nums)
        for i in range(n):
            x=nums[i]
            remaining=target-x
            if remaining in h:
                return [h[remaining],i]
            h[x]=i
            

        