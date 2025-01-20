#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def isBSTTraversal(self, arr):
        for i in range(1,len(arr)):
            if arr[i]<=arr[i-1]:
                return False
        return True
        # Code here

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.isBSTTraversal(nums)
        print(res)
        print("~")
# } Driver Code Ends