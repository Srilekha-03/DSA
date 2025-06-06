class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        ds=[]
        visited=[0]*len(nums)
    
        nums.sort()
        def permutation(nums,index,ds,visited,ans):
            if index==len(nums):
                ans.append(ds[:])
                return
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1] and visited[i-1]==1:
                    continue
                if visited[i]!=1:
                    visited[i]=1
                    ds.append(nums[i])
                    permutation(nums,index+1,ds ,visited,ans)
                    visited[i]=0
                    ds.pop()
        permutation(nums,0,ds,visited,ans)
        return ans
        