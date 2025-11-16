class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        sub=[]
        self.combination(0,candidates,target,sub,ans)
        return ans
    def combination(self,index,candidates,target,sub,ans):
        if index==len(candidates):
            if target==0:
                ans.append(sub[:])
            return
        if candidates[index]<=target:
            sub.append(candidates[index])
            self.combination(index,candidates,target-candidates[index],sub,ans)#picking
            sub.pop()#removing
        self.combination(index+1,candidates,target,sub,ans)
        
        



        