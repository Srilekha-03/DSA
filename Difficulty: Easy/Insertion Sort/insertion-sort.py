#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# Please change the array in-place
class Solution:
    def insertionSort(self, arr):
        n=len(arr)
        for i in range(n):
            j=i
            while j>0 and arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
                #code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.insertionSort(arr)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends