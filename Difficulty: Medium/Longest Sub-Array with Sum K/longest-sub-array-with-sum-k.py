# User function Template for python3

class Solution:
    def lenOfLongestSubarr(self, arr, k): 
        presumdict={}
        maxlen=0
        presum=0
        for i in range(len(arr)):
            presum+=arr[i]
            if presum==k:
                maxlen=max(maxlen,i+1)
            else:
                rem=presum-k
                if rem in presumdict:
                    maxlen=max(maxlen,i-presumdict[rem])
            if presum not in presumdict:
                presumdict[presum]=i
        return maxlen
        
        # code here
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.lenOfLongestSubarr(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends