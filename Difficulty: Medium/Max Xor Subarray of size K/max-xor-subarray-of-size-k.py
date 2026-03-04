class Solution:
    def maxSubarrayXOR(self, arr, k):
        xor=0
        n=len(arr)
        for i in range(k):
            xor^=arr[i]
        ans=xor
        i=0
        j=k
        while j<n:
            xor^=arr[j]
            xor^=arr[i]
            i+=1
            ans=max(ans,xor)
            j+=1
        return ans
        
        
        # code here
        
       