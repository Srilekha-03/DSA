class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        nsee=self.nse(prices)
        for i in range(len(nsee)):
            nsee[i]=prices[i]-nsee[i]
        return nsee

    def nse(self,arr):
        stack=[]
        n=len(arr)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and arr[i]<stack[-1]:
                stack.pop()
            if not stack:
                ans[i]=0
            else:
                ans[i]=stack[-1]
            stack.append(arr[i])
        return ans
        