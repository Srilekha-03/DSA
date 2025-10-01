class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        empty=numBottles
        while empty>=numExchange:
            full=empty//numExchange
            emp=empty%numExchange
            ans+=full
            empty=full+emp
        return ans
        