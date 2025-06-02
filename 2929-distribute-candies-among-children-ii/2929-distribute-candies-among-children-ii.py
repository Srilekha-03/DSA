class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        #calculating min and max for first child and simultaneoulsy ranging the same for 2nd and 3rd and finding total ways
        firstMin=max(0,n-2*limit)
        ways=0
        firstMax=min(n,limit)
        for i in range(firstMin,firstMax+1):
            N=n-i #new range
            mini=max(0,N-limit)
            maxi=min(N,limit)
            ways+=maxi-mini+1
        return ways

        
        