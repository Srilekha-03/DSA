#User function Template for python3
class Solution:
	def subsetSums(self, arr):
	    ans=[]
	    self.subsetsum(0,0,arr,ans)
	    ans.sort()
	    return ans
	def subsetsum(self,index,summ,arr,ans):
	    if index==len(arr):
	        ans.append(summ)
	        return
	    self.subsetsum(index+1,summ+arr[index],arr,ans)
	    self.subsetsum(index+1,summ,arr,ans)
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        arr = [int(x)
               for x in input().split()]  # Reading array for the test case
        ob = Solution()
        ans = ob.subsetSums(arr)  # Getting the subset sums
        ans.sort()  # Sorting the result

        # Printing the subset sums in space-separated format
        for x in ans:
            print(x, end=" ")
        print("")  # Ensuring new line after each test case

# } Driver Code Ends