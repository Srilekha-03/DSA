class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        after=[[0 for i in range(k+1)]for j in range(2)]
        current=[[0 for i in range(k+1)]for j in range(2)]
        
        for i in range(len(prices)-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy==1:
                        current[buy][cap]=max(-prices[i]+after[0][cap],0+after[1][cap])
                    else:
                        current[buy][cap]=max(prices[i]+after[1][cap-1],0+after[0][cap])
            after = [row[:] for row in current]
        return after[1][k]
        