#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
MOD = 1000000007
class Solution:
    def topDown(self, n):
        v={}
        return self.dp(n,v)
    def dp(self,n,v):
        if n<=1:
            return n
        if n in v:
            return v[n]
        v[n]=(self.dp(n-1,v)+self.dp(n-2,v))% MOD
        return v[n]
            
            
        # Code here
    def bottomUp(self, n):
        if n <= 1:
            return n
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=(dp[i-1]+dp[i-2])% MOD
        return dp[n]
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        topDownans=ob.topDown(n);
        bottomUpans=ob.bottomUp(n);
        if(topDownans!=bottomUpans):
            print(-1)
        else:
            print(bottomUpans)
        print("~")
# } Driver Code Ends