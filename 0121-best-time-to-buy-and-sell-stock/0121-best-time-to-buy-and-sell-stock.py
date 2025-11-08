class Solution(object):
    def maxProfit(self, prices):
        minn=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cost=prices[i]-minn
            profit=max(cost,profit)
            minn=min(minn,prices[i])
        return profit
        
        