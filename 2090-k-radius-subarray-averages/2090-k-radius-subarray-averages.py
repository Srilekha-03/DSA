class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        prefix=[-1]*n
        res=[-1]*n

        if k==0: 
            return nums
        if 2*k+1>n: 
            return res

        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+nums[i]
        for i in range(k,n-k):
            summ=prefix[i+k]
            if i-k>0:
                summ-=prefix[i-k-1]
            res[i]=summ//(2*k+1)
        return res

            

        