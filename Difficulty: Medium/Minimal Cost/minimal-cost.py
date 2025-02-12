#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        dp=[0]*len(arr)
        dp[0]=0
        for i in range(1,len(arr)):
            mini=float('inf')
            for j in range(1,k+1):
                if i-j>=0:
                    jump=dp[i-j]+abs(arr[i]-arr[i-j])
                    mini=min(mini,jump)
            dp[i]=mini
        return dp[-1]
                
        # code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(k,arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends