class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            x = self.partition(arr, low, high)
            self.quickSort(arr, low, x - 1)
            self.quickSort(arr, x + 1, high)
    
    def partition(self, arr, low, high):
        p = arr[low]  # Pivot element
        i = low + 1
        j = high
        
        while True:
            # Move i to the right until an element greater than pivot is found
            while i <= high and arr[i] <= p:
                i += 1
            # Move j to the left until an element smaller than or equal to pivot is found
            while j >= low and arr[j] > p:
                j -= 1
            
            if i >= j:  # Pointers have crossed; break the loop
                break
            
            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]
        
        # Swap pivot with the element at j (final position of pivot)
        arr[low], arr[j] = arr[j], arr[low]
        return j
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().split()))
        n = len(arr)
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
        print("~")

# } Driver Code Ends