class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem={}
        def solve(i,boo,mem):
            if i>=len(prices):
                return 0
            if (i,boo) in mem:
                return mem[(i,boo)]
            if boo:
                buy=-prices[i]+solve(i+1,0,mem)
                skip=solve(i+1,1,mem)
                mem[(i,boo)]=max(buy,skip)
                return mem[(i,boo)]
            else:
                sell=prices[i]+solve(i+1,1,mem)
                skip=solve(i+1,0,mem)
                mem[(i,boo)]=max(sell,skip)
                return max(sell,skip)
        return solve(0,1,mem)
        