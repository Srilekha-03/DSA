#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def mergeSort(self, arr, l, h):
        if l >= h:
            return
        mid = l + (h - l) // 2
        self.mergeSort(arr, l, mid)  
        self.mergeSort(arr, mid + 1, h) 
        self.merge(arr, l, mid, h)
    
    def merge(self, arr, l, mid, h):
        t = []
        left = l
        right = mid + 1
        while left <= mid and right <= h:
            if arr[left] <= arr[right]:
                t.append(arr[left])
                left += 1
            else:
                t.append(arr[right])
                right += 1
        while left <= mid:
            t.append(arr[left])
            left += 1
        while right <= h:
            t.append(arr[right])
            right += 1
        for i in range(l, h + 1):
            arr[i] = t[i - l]
            
        
            
                
            
        #code here


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends