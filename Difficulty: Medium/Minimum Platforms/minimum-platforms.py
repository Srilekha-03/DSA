#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        i=0
        j=0
        maxcount=-1
        count=0
        n=len(arr)
        while i<n:
            if arr[i]<=dep[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            maxcount=max(maxcount,count)
        return maxcount
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends