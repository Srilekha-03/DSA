#User function Template for python3

class Solution:
	def nthRoot(self, n: int, m: int) -> int:
	    low=1
        high=m
        while low<=high:
            mid=(low+high)//2
            if mid**n==m:
                return mid
            elif mid**n<m:
                low=mid+1
            else:
                high=mid-1
        return -1
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        m = int(input())
        ob = Solution()
        ans = ob.nthRoot(n, m)
        print(ans)

# } Driver Code Ends