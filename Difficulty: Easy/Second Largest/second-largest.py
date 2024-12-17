#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        l=arr[0]
        sl=-1
        for i in arr:
            if i>l:
                sl=l
                l=i
            if i<l and i>sl:
                sl=i
        return sl
        # Code Here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends