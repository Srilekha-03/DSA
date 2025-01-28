#User function Template for python3
class Solution:
    def isEven (self, n):
        return (n & 1) == 0
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        if ob.isEven(N):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends