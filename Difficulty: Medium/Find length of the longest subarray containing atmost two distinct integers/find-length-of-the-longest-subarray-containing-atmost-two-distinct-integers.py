#User function Template for python3

class Solution:
    def totalElements(self,arr):
        r=0
        l=0
        maxlen=0
        d=dict()
        while r<len(arr):
            if arr[r] not in d:
                d[arr[r]]=0
            d[arr[r]]+=1   
            while len(d)>2:
                d[arr[l]]-=1
                if d[arr[l]]==0:
                    del d[arr[l]]
                l+=1
            
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
            
        
        
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        # N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.totalElements(arr)
        print(res)
        print("~")

# } Driver Code Ends