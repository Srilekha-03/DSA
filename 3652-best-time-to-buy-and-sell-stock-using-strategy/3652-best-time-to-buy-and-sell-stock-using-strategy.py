class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        tot=0
        n=len(prices)
        for i in range(n):
            tot+=(prices[i]*strategy[i])
        ans=tot
        window1=0
            
        for i in range(k):
            window1+=(prices[i]*strategy[i])

        l1=0
        r1=k-1
        l2=0
        m2=(k//2)
        r2=k-1
        window2=0
        for i in range(m2,r2+1):
            window2+=prices[i]
        ans=max(ans,tot-window1+window2)
        while r1<n-1:
            window1-=(prices[l1]*strategy[l1])
            l1+=1
            window1+=(prices[r1+1]*strategy[r1+1])
            r1+=1
            window2-=(prices[m2])
            m2+=1
            l2+=1
            window2+=(prices[r2+1])
            r2+=1
            ans=max(ans,tot-window1+window2)
        return ans