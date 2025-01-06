#User function Template for python3
class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        items=[(val[i],wt[i],val[i]/wt[i]) for i in range(len(val))]
        items.sort(key=lambda x:x[2],reverse=True)
        total=0
        for val,wt,ratio in items:
            if capacity>wt:
                total+=val
                capacity-=wt
            else:
                total+=ratio*capacity
                break
        return total
        #code here


#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        # Read values array
        values = list(map(int, input().strip().split()))

        # Read weights array
        weights = list(map(int, input().strip().split()))

        # Read the knapsack capacity
        W = int(input().strip())

        ob = Solution()
        print("%.6f" % ob.fractionalknapsack(values, weights, W))
        print("~")

# } Driver Code Ends