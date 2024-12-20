class Solution:
    def leaders(self, arr):
        n=len(arr)
        maxy=float('-inf')
        leaders=[]
        for i in range(n-1,-1,-1):
            if arr[i]>=maxy:
                leaders.append(arr[i])
                maxy=max(maxy,arr[i])
        return leaders[::-1]
        
        # code here


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends