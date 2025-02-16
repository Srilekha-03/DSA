class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for i in range(2)]for j in range(n+1)]
        dp[n][0],dp[n][1]=0,0
        for index in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy==1:
                    profit=max(-prices[index]+dp[index+1][0], 0+dp[index+1][1])
                else:
                    profit=max(prices[index]+dp[index+1][1],0+dp[index+1][0])
                dp[index][buy]=profit
        return dp[0][1]
        