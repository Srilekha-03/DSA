#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math
class Solution:
    def solve(self, bt):
        n=len(bt)
        bt.sort()
        waitingTime=0
        time=0
        for i in range(n):
            waitingTime+=time
            time+=bt[i]
        return math.floor(waitingTime/n)
            
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        bt = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(bt)
        print(res)
        print("~")
# } Driver Code Ends