#User function Template for python3

class Solution:
    def findTwoElement( self,arr):
        n=len(arr)
        sn=(n*(n+1))/2
        s2n=(n*(n+1)*((2*n)+1))/6
        s=0
        s2=0
        for i in arr:
            s+=i
            s2+=i*i
        val1=s-sn
        val2=s2-s2n
        val2=val2/val1
        X=(val1+val2)/2
        Y=X-val1
        return [int(X),int(Y)]
        
        # code here




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends