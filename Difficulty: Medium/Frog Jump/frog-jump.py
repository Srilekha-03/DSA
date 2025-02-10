#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys


# } Driver Code Ends
#User function Template for python3
class Solution:
    def minCost(self, height):
        prev1=0
        prev2=0
        for i in range(1,len(height)):
            left=prev1+abs(height[i]-height[i-1])
            right=float('inf')
            if i>1:
                right=prev2+abs(height[i]-height[i-2])
            cur=min(left,right)
            prev2=prev1
            prev1=cur
        return prev1
                
        # code here

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    
    pointer = 0
    
    t = int(input_lines[pointer].strip())
    pointer += 1
    
    for _ in range(t):
        arr = list(map(int, input_lines[pointer].strip().split()))
        pointer += 1
        
        ob = Solution()
        print(ob.minCost(arr))
        print("~")

# } Driver Code Ends