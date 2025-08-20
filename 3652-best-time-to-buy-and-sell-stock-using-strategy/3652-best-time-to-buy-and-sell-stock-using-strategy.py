class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        original=0
        n=len(prices)
        for i in range(n):
            original+=prices[i]*strategy[i]
        for i in range(n-k+1):
            window=0
            w=strategy[i:i+k]
            w[:k//2]=[0]*(k//2)
            w[k//2:]=[1]*(k//2)
            new=strategy[:]
            new[i:i+k]=w
            for j in range(n):
                window+=prices[j]*new[j]
            original=max(window,original)
        return original
            
            
        