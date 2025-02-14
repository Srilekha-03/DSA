#User function Template for python3

class Solution:
    def maximumPoints(self, arr):
        prev=[0]*4
        prev[0]=max(arr[0][1],arr[0][2])
        prev[1]=max(arr[0][0],arr[0][2])
        prev[2]=max(arr[0][0],arr[0][1])
        prev[3]=max(arr[0][0],arr[0][2])
        for day in range(1,len(arr)):
            temp=[0]*4
            for last in range(4):
                temp[last]=0
                for task in range(3):
                    if task!=last:
                        temp[last]=max(temp[last],arr[day][task]+prev[task])
            prev=temp
        return max(prev)
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        ob = Solution()
        print(ob.maximumPoints(arr))
        print("~")
# } Driver Code Ends