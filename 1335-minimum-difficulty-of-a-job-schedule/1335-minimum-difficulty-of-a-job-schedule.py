class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n=len(jobDifficulty)
        if n<d:
            return -1
        i=0
        from functools import lru_cache

        @lru_cache(None)
        def solve(i,d):
            if d==1:
                return max(jobDifficulty[i:n])
            maxd=jobDifficulty[i]
            mini=float('inf')
            for j in range(i,n-d+1):
                maxd=max(maxd,jobDifficulty[j])
                res=maxd+solve(j+1,d-1)
                mini=min(mini,res)
            return mini
        return solve(i,d)
        