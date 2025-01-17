class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        sub=[]
        nums.sort()
        self.subset(0,nums,sub,ans)
        return ans
    def subset(self,index,nums,sub,ans):
        ans.append(sub[:])
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            sub.append(nums[i])
            self.subset(i+1,nums,sub,ans)
            sub.pop()
        