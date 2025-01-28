#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def get(self, a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        return a, b
        #code here

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		a,b = map(int,input().strip().split())
		ob = Solution()
		ans=ob.get(a,b)
		print(str(ans[0])+" "+str(ans[1]))
# } Driver Code Ends