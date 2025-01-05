class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        nse=self.nse(arr)
        pse=self.pse(arr)
        total=0
        for i in range(len(arr)):
            left=i-pse[i]
            right=nse[i]-i
            total+=((left*right)*arr[i])%mod
        return total%mod
    def nse(self,arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            ans[i]=stack[-1] if stack else n
            stack.append(i)
        return ans
    def pse(self,arr):
        n=len(arr)
        stack=[]
        ans=[0]*n
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            ans[i]=stack[-1] if stack else -1
            stack.append(i)
        return ans
             
        