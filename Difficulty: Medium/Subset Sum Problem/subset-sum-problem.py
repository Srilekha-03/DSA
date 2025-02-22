#User function Template for python3

class Solution:
    def isSubsetSum (self, arr, target):
        dp=[[-1 for i in range(target+1)]for j in range(len(arr))]
        return self.recursion(len(arr)-1,arr,target,dp)
    def recursion(self,index,arr,target,dp):
        if target==0:
            return True
        if index==0:
            return arr[0]==target
        if dp[index][target]!=-1:
            return dp[index][target]
        not_take=self.recursion(index-1,arr,target,dp)
        take=False
        if target>=arr[index]:
            take=self.recursion(index-1,arr,target-arr[index],dp)
        dp[index][target]= take or not_take
        return dp[index][target]
            
        # code here 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends