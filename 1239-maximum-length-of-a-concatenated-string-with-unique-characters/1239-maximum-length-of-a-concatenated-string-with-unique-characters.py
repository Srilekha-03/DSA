class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n=len(arr)
        temp=""
        i=0

        def isDup(temp, new):
            combined = temp + new
            return len(combined) != len(set(combined))

        def solve(i,arr,temp,n):
            if i>=n:
                return len(temp)
            take=0
            if isDup(temp,arr[i]):
                notTake=solve(i+1,arr,temp,n)
            else:
                take=solve(i+1,arr,temp+arr[i],n)
                notTake=solve(i+1,arr,temp,n)
            return max(take,notTake)

        return solve(0,arr,temp,n)

        