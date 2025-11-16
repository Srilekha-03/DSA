class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        l=[]
        n=len(candidates)
        def solve(i):
            if sum(l)==target:
                res.append(l.copy())
                return 
            if sum(l)>target:
                return
            for j in range(i,n):
                l.append(candidates[j])
                solve(j)
                l.pop()
        solve(0)
        return res
