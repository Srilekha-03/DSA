#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        maxsum=float('-inf')
        for i in range(1,len(arr)):
            if arr[i]+arr[i-1]>maxsum:
                maxsum=arr[i]+arr[i-1]
        return maxsum
        # Your code goes here
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends