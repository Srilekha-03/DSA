class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        noOfSubsets=1<<len(nums)
        ans=[]
        for i in range(noOfSubsets):
            l=[]
            for j in range(len(nums)):
                if i & 1<<j:
                    l.append(nums[j])
            ans.append(l)
        return ans
        