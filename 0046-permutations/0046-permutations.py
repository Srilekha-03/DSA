class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def permutation(nums,index,ans):
            if index==len(nums):
                ans.append(nums[:])
                return
            for i in range(index,len(nums)):
                nums[i],nums[index]=nums[index],nums[i]
                permutation(nums,index+1,ans)
                nums[i],nums[index]=nums[index],nums[i]                  
        permutation(nums,0,ans)
        return ans
                
        