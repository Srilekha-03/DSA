class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        ahead=[0]*2
        cur=[0]*2
        ahead[0],ahead[1]=0,0
        for index in range(n-1,-1,-1):
            for buy in range(2):
                profit=0
                if buy==1:
                    profit=max(-prices[index]+ahead[0], 0+ahead[1])
                else:
                    profit=max(prices[index]+ahead[1],0+ahead[0])
                cur[buy]=profit
            ahead=cur       
        return ahead[1]
        