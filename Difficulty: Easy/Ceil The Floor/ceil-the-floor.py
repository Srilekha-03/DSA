#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        arr.sort()
        res=[]
        res.append(self.Floor(x,arr))
        res.append(self.Ceil(x,arr))
        return res
    def Floor(self, x: int, arr: list):
        n=len(arr)
        ans=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<=x:
                ans=arr[mid]
                low=mid+1
            else:
                high=mid-1
        return ans
    def Ceil(self, x: int, arr: list):
        n=len(arr)
        ans=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=arr[mid]
                high=mid-1
            else:
                low=mid+1
                
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends