class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,arr,k):
        n=len(arr)
        low=0
        high=n-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<=k:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
        #Your code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends