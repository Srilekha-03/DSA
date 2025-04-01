#User function Template for python3

class Solution:
    def nthRoot(self, n: int, m: int) -> int:
        def function(mid,n,m):
            ans=1
            for i in range(n):
                ans=ans*mid
                if ans>m:
                    return 2
            if ans==m:
                return 1
            return 0
                
        low=1
        high=m
        while low<=high:
            mid=(low+high)//2
            midNth=function(mid,n,m)
            if midNth==1:
                return mid
            elif midNth==0:
                low=mid+1
            else:
                high=mid-1
        return -1
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        m = int(input())
        ob = Solution()
        ans = ob.nthRoot(n, m)
        print(ans)
        print("~")

# } Driver Code Ends