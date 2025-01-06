#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        time=[(start[i],end[i]) for i in range(len(start))]
        time.sort(key=lambda x:x[1])
        count=1
        end=time[0][1]
        for i in range(1,len(time)):
            if time[i][0]>end:
                count+=1
                end=time[i][1]
        return count
            
            
            
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
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(start, end))
        print("~")

# } Driver Code Ends