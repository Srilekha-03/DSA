#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        u=[]
        i=0
        j=0
        while(i<len(a) and j <len(b)):
            if a[i]<=b[j]:
                if len(u)==0 or u[-1]!=a[i]:
                    u.append(a[i])
                i+=1
            else:
                if len(u)==0 or u[-1]!=b[j]:
                    u.append(b[j])
                j+=1
        while i<len(a):
            if len(u)==0 or u[-1]!=a[i]:
                u.append(a[i])
            i+=1
        while j <len(b):
            if len(u)==0 or u[-1]!=b[j]:
                u.append(b[j])
            j+=1
        return u
            
            
                
                
                
                
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")

# } Driver Code Ends