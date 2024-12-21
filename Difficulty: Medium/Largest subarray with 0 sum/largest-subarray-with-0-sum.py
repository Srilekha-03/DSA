#Your task is to complete this function
 
class Solution:
    def maxLen(self, arr):
        n=len(arr)
        maxlen=0
        presum=0
        h=dict()
        for i in range(n):
            presum+=arr[i]
            if presum==0:
                maxlen=i+1
            else:
                if presum in h:
                    maxlen=max(maxlen,i-h[presum])
                else:
                    h[presum]=i
        return maxlen
        # code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(arr))
        print("~")

# } Driver Code Ends