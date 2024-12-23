#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        n=len(arr)
        mini=float('inf')
        k=0
        low=0
        high=n-1
        while low<=high:
            mid=low+(high-low)//2
            if arr[low]<arr[high]:
                if arr[low]<mini:
                    k=low
                    mini=arr[low]
                return k
            if arr[low]<=arr[mid]:
                if arr[low]<mini:
                    k=low
                    mini=arr[low]
                low=mid+1
            else:
                if arr[mid]<mini:
                    k=mid
                    mini=arr[mid]
                high=mid-1
        return k

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)
        print("~")
# } Driver Code Ends