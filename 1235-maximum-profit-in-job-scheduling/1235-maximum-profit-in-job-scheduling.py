class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n=len(profit)
        arr=[[startTime[i],endTime[i],profit[i]] for i in range(n)]
        arr.sort(key= lambda x:(x[0],x[1]))
        d=dict()
        def nextt(l,target):
            h=n-1
            nex=n
            while l<=h:
                m=l+(h-l)//2
                if arr[m][0]>=target:
                    nex=m
                    h=m-1
                else:
                    l=m+1
            return nex
        def solve(i):
            if i>=n:
                return 0
            if i in d:
                return d[i]
            take=arr[i][2]+solve(nextt(i+1,arr[i][1]))
            nottake=solve(i+1)
            d[i]=max(take,nottake)
            return d[i]
        return solve(0)
        